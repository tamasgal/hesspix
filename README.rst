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

  >>> r.get_event(0)
  rec.array([(696, 15.363794 , 3, 21.796875),
             (702,  9.463919 , 3, 21.828125),
             (854,  8.21018  , 3, 20.34375 ),
             (862,  7.8234243, 3, 21.59375 ),
             (880, 19.85337  , 3, 20.578125),
             (889, 19.890633 , 3, 19.875   ),
             (890,  8.490422 , 3, 18.890625),
             (897, 11.9091625, 3, 20.46875 ),
             (898,  8.9501295, 3, 20.265625),
             (899, 18.064999 , 3, 20.      )],
            dtype=[('id', '<i4'), ('intensity', '>f4'), ('channel', 'i1'), ('time', '>f4')])

  >>> for event in r:
          ...

Installation
~~~~~~~~~~~~

It is recommended to first create an isolated virtualenvironment to not interfere
with other Python projects::

  git clone https://git.ecap.work/tgal/hesspix
  cd hesspix
  python3 -m venv venv
  . venv/bin/activate

Install directly from the Git server via ``pip`` (no cloneing needed)::

  pip install git+https://git.ecap.work/tgal/hesspix

Or clone the repository and run::

  make install

To install all the development dependencies, in case you want to contribute or
run the test suite::

  make install-dev
  make test


---

*Created with ``cookiecutter https://git.km3net.de/templates/python-project``*
