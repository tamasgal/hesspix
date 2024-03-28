hesspix 
=======

.. image:: https://git.ecap.work/tgal/hesspix/badges/master/pipeline.svg
    :target: https://git.ecap.work/tgal/hesspix/pipelines

.. image:: https://git.ecap.work/tgal/hesspix/badges/master/coverage.svg
    :target: https://tgal.pages.ecap.work/hesspix/coverage

.. image:: https://git.km3net.de/examples/km3badges/-/raw/master/docs-latest-brightgreen.svg
    :target: https://tgal.pages.ecap.work/hesspix

``hesspix`` is a tiny library to read HESS pixel info from ROOT files.

Usage
~~~~~

It's as easy as::

    >>> import hesspix as hp

    >>> r = hp.CT5Reader("gamma_20deg_180deg_run4151.dst.root")

    >>> r[0]
    Event 801 (bunch 0) [10 pixels]

    >>> r[23]
    Event 19607 (bunch 0) [3 pixels]

    >>> r.get(event_nr=3902, bunch_nr=0)
    Event 3902 (bunch 0) [18 pixels]

    >>> event = r.get(event_nr=3902, bunch_nr=0)

    >>> event.pixinfo
    rec.array([( 352, 18.27153 , 3, 20.9375  ),
            ( 353, 23.193665, 3, 21.703125),
            ( 355, 11.846128, 3, 22.171875),
            ( 357, 15.300814, 3, 21.5     ),
            ( 513,  8.219065, 3, 21.046875),
            (1296, 15.051192, 3, 19.890625),
            (1299,  9.525627, 3, 19.265625),
            (1302,  9.479142, 3, 20.21875 ),
            (1304, 14.532091, 3, 21.171875),
            (1306, 22.21212 , 3, 21.46875 ),
            (1307, 11.263601, 3, 20.953125),
            (1316, 16.932125, 3, 20.046875),
            (1318, 13.045629, 3, 21.515625),
            (1324, 13.618393, 3, 20.75    ),
            (1325, 12.267553, 3, 20.953125),
            (1329,  8.492023, 3, 21.921875),
            (1339, 10.908205, 3, 20.953125),
            (1341, 21.191723, 3, 21.546875)],
            dtype=[('id', '<i4'), ('intensity', '>f4'), ('channel', 'i1'), ('time', '>f4')])

    >>> for event in r:
            ...

Installation
~~~~~~~~~~~~

``hesspix`` is a registered Python package. It can be installed using ``pip``::

  pip install hesspix

To install the latest development version from the Git repository::

  pip install git+https://github.com/tamasgal/hesspix

Or clone the repository and run::

  make install

To install all the development dependencies, in case you want to contribute or
run the test suite::

  make install-dev
  make test


---

*Created with ``cookiecutter https://git.km3net.de/templates/python-project``*
