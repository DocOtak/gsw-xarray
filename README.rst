.. |CI Status| image:: https://github.com/docotak/gsw-xarray/actions/workflows/ci.yml/badge.svg
  :target: https://github.com/DocOtak/gsw-xarray/actions/workflows/ci.yml
  :alt: CI Status
.. |Documentation Status| image:: https://readthedocs.org/projects/gsw-xarray/badge/?version=latest
  :target: https://gsw-xarray.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

gsw-xarray: Wrapper for gsw that adds CF attributes
===================================================
|CI Status| |Documentation Status|

gsw-xarray is a wrapper for `gsw python <https://github.com/TEOS-10/GSW-python>`_
that will add CF attributes to xarray.DataArray outputs.
It is meant to be a drop in wrapper for the upstream GSW-Python library and will only add these attributes if one argument to a function is an xarray.DataArray.

You can find the documentation on `gsw-xarray.readthedocs.io <https://gsw-xarray.readthedocs.io/>`_.

Usage
-----

.. code:: python

   import gsw_xarray as gsw

   # Create a xarray.Dataset
   import numpy as np
   import xarray as xr
   ds = xr.Dataset()
   id = np.arange(3)
   ds['id'] = xr.DataArray(id, coords={'id':id})
   ds['CT'] = ds['id'] * 10
   ds['CT'].attrs = {'standard_name':'sea_water_conservative_temperature'}
   ds['SA'] = ds['id'] * 0.1 + 34
   ds['SA'].attrs = {'standard_name':'sea_water_absolute_salinity'}

   # Apply gsw functions
   sigma0 = gsw.sigma0(SA=ds['SA'], CT=ds['CT'])
   print(sigma0.attrs)

Outputs

::

   {'standard_name': 'sea_water_sigma_t', 'units': 'kg/m^3'}

Don't worry about usage with non xarray array objects, just use in all places you would the upstream library:

.. code:: python

   sigma0 = gsw.sigma0(id * 10, id * 0.1 + 34)
   print(type(sigma0), sigma0)

Outputs

::

   <class 'numpy.ndarray'> [-5.08964499  2.1101098   9.28348219]


We support (but don't yet validate) the usage of pint.Quantities and the usage of xarray wrapped Quantities.
Support for pint requires the installation of two optional dependencies: `pint` and `pint-xarray`.
If any of the inputs to a gsw function are Quantities, the returned object will also be a Quantity belonging to the same UnitRegistry.

.. warning::
   Quantities must all belong to the same pint.UnitRegistry, a ValueError will be thrown if there are mixed registries.

.. code:: python
   import pint_xarray
   import gsw_xarray as gsw

   # Create a xarray.Dataset
   import numpy as np
   import xarray as xr
   ds = xr.Dataset()
   id = np.arange(3)
   ds['id'] = xr.DataArray(id, coords={'id':id})
   ds['CT'] = ds['id'] * 10
   # make sure there are unit attrs this time
   ds['CT'].attrs = {'standard_name':'sea_water_conservative_temperature', 'units': 'degC'}
   ds['SA'] = ds['id'] * 0.1 + 34
   ds['SA'].attrs = {'standard_name':'sea_water_absolute_salinity', 'units': 'g/kg'}

   # use the pint accessor to quantify things
   ds = ds.pint.quantify()

   # Apply gsw functions
   sigma0 = gsw.sigma0(SA=ds['SA'], CT=ds['CT'])
   # outputs are now quantities!
   print(sigma0)

Outputs

::
   <xarray.DataArray 'sigma0' (id: 3)>
   <Quantity([27.17191038 26.12820162 24.03930887], 'kilogram / meter ** 3')>
   Coordinates:
     * id       (id) int64 0 1 2
   Attributes:
       standard_name:  sea_water_sigma_t

The usage of xarray wrapped Quantities is not required, you can use pint directly (though the `pint-xarray` dep still needs to be installed).

.. code:: python

   import gsw_xarray as gsw
   import pint
   ureg = pint.UnitRegistry()
   SA = ureg.Quantity(35, ureg("g/kg"))
   CT = ureg.Quantity(10, ureg.degC)
   sigma0 = gsw.sigma0(SA=SA, CT=CT)
   print(sigma0)

Outputs

::
   26.824644457868317 kilogram / meter ** 3

Installation
------------
Pip
...

.. code:: bash

    pip install gsw_xarray


Conda
.....

For the moment gsw-xarray is not released in conda-forge, so you'll
need to install via pip: activate your conda environment, and then use ``pip install gsw_xarray``.

Pipenv
......

Inside a pipenv environment: ``pipenv install gsw_xarray``.


Contributor guide
-----------------

All contributions, bug reports, bug fixes, documentation improvements,
enhancements, and ideas are welcome.
If you notice a bug or are missing a feature, fell free
to open an issue in the `GitHub issues page <https://github.com/DocOtak/gsw-xarray/issues>`_.

In order to contribute to gsw-xarray, please fork the repository and
submit a pull request. A good step by step tutorial for starting with git can be found in the
`xarray contributor guide <https://xarray.pydata.org/en/stable/contributing.html#working-with-the-code>`_.
A main difference is that we do not use conda as python environment, but poetry.

Set up the environment
......................

You will first need to `install poetry <https://python-poetry.org/docs/#installation>`_.
Then go to your local clone of gsw-xarray and launch installation:

.. code:: bash

   cd /path/to/your/gsw-xarray
   poetry install

You can then activate the environment by launching a shell
within the virtual environment:

.. code:: bash

   poetry shell

You can check that the tests pass locally:

.. code:: bash

   pytest gsw_xarray/tests

Release (for maintainers only)
..............................

TODO...
