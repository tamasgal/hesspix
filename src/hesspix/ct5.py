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
    def __init__(self, filename, branch="DST_tree/IntensityData_Clean0714NN2_5"):
        self._fobj = f = uproot.open(filename)
        self._event_nrs = f["DST_tree/EventHeader/fGlobalEvtNum"].array()
        self._bunch_nrs = f["DST_tree/EventHeader/fGlobalBunchNum"].array()
        self._branch = branch

        self._nevents = len(self._event_nrs)

    def __len__(self):
        return self._nevents

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        if self._idx < len(self):
            event = self[self._idx]
            self._idx += 1
            return event
        else:
            raise StopIteration

    def get(self, event_nr=0, bunch_nr=0):
        """
        Get event with a given event number and bunch number.
        """
        indices = np.where((self._event_nrs == event_nr) & (self._bunch_nrs == bunch_nr))[0]
        if len(indices) == 1:
            return self[indices[0]]
        elif len(indices) == 0:
            raise IndexError(f"No event found with event number '{event_nr}' in bunch '{bunch_nr}'")
        else:
            raise ValueError("Multiple events found with the same event number and bunch number")

    def get_bunch(self, bunch_nr):
        """
        Get all events for a given bunch number.
        """
        indices = np.where(self._bunch_ids == bunch_nr)[0]
        return [self[idx] for idx in indices]

    def __getitem__(self, idx):
        """
        Get event of a given event ID (index in the file).
        """
        raw = self._fobj[self._branch].array(
            uproot.interpretation.jagged.AsJagged(
                uproot.interpretation.numerical.AsDtype("b"),
                header_bytes=0),
            entry_start=idx,
            entry_stop=idx+1
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

        pixmask = np.frombuffer(s.read(masknbytes), dtype="u1")
        npix = count_set_bits(pixmask)

        size = read_uint(s)  # total number of pixels

        intensity_data_mode = read_uint(s)

        if intensity_data_mode != 2: # enum value for `All`, presumable
            raise ValueError(f"Unsupported intensity data mode: {intensity_data_mode}")

        return Event(
            self._event_nrs[idx],
            self._bunch_nrs[idx],
            np.core.records.fromarrays(
                [
                    np.array(pixmask2pixelids(pixmask), dtype="i"),
                    np.frombuffer(s.read(npix*4), dtype=">f"),
                    np.frombuffer(s.read(npix), dtype="b"),
                    np.frombuffer(s.read(npix*4), dtype=">f")
                ],
                names=["id", "intensity", "channel", "time"]
            )
        )


class Event:
    def __init__(self, event_nr, bunch_nr, pixinfo):
        self.event_nr = event_nr
        self.bunch_nr = bunch_nr
        self.pixinfo = pixinfo

    def __repr__(self):
        return f"Event {self.event_nr} (bunch {self.bunch_nr}) [{len(self.pixinfo)} pixels]"


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
    """
    return np.where(np.unpackbits(mask, bitorder="little"))[0]


def count_set_bits(arr):
    """
    Count the number of set bits in an array of uint8.
    """
    return np.count_nonzero(np.unpackbits(arr))
