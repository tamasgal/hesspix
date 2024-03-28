hesspix 
=======

.. image:: https://git.ecap.work/tgal/hesspix/badges/master/pipeline.svg
    :target: https://git.ecap.work/tgal/hesspix/pipelines

.. image:: https://git.ecap.work/tgal/hesspix/badges/master/coverage.svg
    :target: https://tgal.pages.ecap.work/hesspix/coverage

.. image:: https://git.km3net.de/examples/km3badges/-/raw/master/docs-latest-brightgreen.svg
    :target: https://tgal.pages.ecap.work/hesspix

``hesspix`` is a tiny library to read HESS pixel info from ROOT files.

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
