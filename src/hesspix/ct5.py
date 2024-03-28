#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import struct
import uproot
import numpy as np


class CT5Reader:
    """
    Reader class for CT5 pixel intensity data.
    """
    def __init__(self, filename):
        self._fobj = f = uproot.open(filename)
        self._event_ids = f["DST_tree/EventHeader/fGlobalEvtNum"].array()
        self._bunch_ids = f["DST_tree/EventHeader/fGlobalBunchNum"].array()

        self._nevents = len(self._event_ids)

    def __len__(self):
        return self._nevents

    def __iter__(self):
        self._current_event_id = 0
        return self

    def __next__(self):
        if self._current_event_id < len(self):
            event = self.get_event(self._current_event_id)
            self._current_event_id += 1
            return event
        else:
            raise StopIteration

    def get_bunch(self, bunch_id):
        """
        Get events for a given bunch ID.
        """
        indices = np.where(self._bunch_ids == bunch_id)[0]
        return [self.get_event(idx) for idx in indices]

    def get_event(self, event_id):
        """
        Get event of a given event ID.
        """
        raw = self._fobj["DST_tree/IntensityData_Clean0714NN2_5"].array(
            uproot.interpretation.jagged.AsJagged(
                uproot.interpretation.numerical.AsDtype("b"),
                header_bytes=0),
            entry_start=event_id,
            entry_stop=event_id+1
        )
        s = io.BytesIO(np.array(raw))

        fName = read_string(s)
        if fName != 'Sash::IntensityData':
            raise ValueError(f"Invalid Sash::IntensityData (fName = {fName})")
        fTitle = read_string(s)

        # TODO: skipping some header stuff
        s.read(48)

        masknbytes = read_uint(s)
        s.read(1)  # skip 1 byte, no idea why

        pixmask = s.read(masknbytes)
        npix = count_set_bits(pixmask)

        size = read_uint(s)  # total number of pixels

        intensity_data_mode = read_uint(s)

        if intensity_data_mode != 2: # enum value for `All`, presumable
            raise ValueError(f"Unsupported intensity data mode: {intensity_data_mode}")

        return np.core.records.fromarrays(
            [
                np.array(pixmask2pixelids(pixmask), dtype="i"),
                np.frombuffer(s.read(npix*4), dtype=">f"),
                np.frombuffer(s.read(npix), dtype="b"),
                np.frombuffer(s.read(npix*4), dtype=">f")
            ],
            names=["id", "intensity", "channel", "time"]
        )


class Event:
    def __init__(self, event_id, bunch_id, pixinfo):
        self.event_id = event_id
        self.bunch_id = bunch_id
        self.pixinfo = pixinfo


def read_uint(bytestream):
    return struct.unpack(">I", bytestream.read(4))[0]


def read_string(bytestream):
    n = 0
    while True:
        _n = struct.unpack("b", bytestream.read(1))[0]
        n += _n
        if _n != 255:
            break
    if n == 0:
        return ""
    return bytestream.read(n).decode()


def pixmask2pixelids(mask):
    """
    Converts a pixel mask to pixel IDs by returning the indices of set
    bits in the mask.

    This function is rather slow and a good candidate for Numba.
    """
    pixel_ids = []
    for i, num in enumerate(mask):
        for j in range(8):
            if num & (1 << j):
                pixel_ids.append(i*8 + j)
    return pixel_ids


def count_set_bits(arr):
    """
    Count the number of set bits in an array of integers.
    """
    count = 0
    for num in arr:
        for j in range(8):
            count += (num >> j) & 1
    return count
