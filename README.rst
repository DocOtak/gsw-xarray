.. |CI Status| image:: https://github.com/docotak/gsw-xarray/actions/workflows/ci.yml/badge.svg
  :target: https://github.com/DocOtak/gsw-xarray/actions/workflows/ci.yml
  :alt: CI Status
.. |Documentation Status| image:: https://readthedocs.org/projects/gsw-xarray/badge/?version=latest
  :target: https://gsw-xarray.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status
.. |pypi| image:: https://badge.fury.io/py/gsw-xarray.svg
   :target: https://badge.fury.io/py/gsw-xarray
   :alt: pypi package
.. |conda forge| image:: https://img.shields.io/conda/vn/conda-forge/gsw-xarray
   :target: https://anaconda.org/conda-forge/gsw-xarray
.. |zenodo| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.8297618.svg
   :target: https://doi.org/10.5281/zenodo.8297618
   :alt: zenodo DOI

gsw-xarray: Wrapper for gsw that adds CF attributes
===================================================
|CI Status| |Documentation Status| |pypi| |conda forge| |zenodo|

gsw-xarray is a wrapper for `gsw python <https://github.com/TEOS-10/GSW-python>`_
that will add CF attributes to xarray.DataArray outputs.
It is meant to be a drop in wrapper for the upstream GSW-Python library and will only add these attributes if one argument to a function is an xarray.DataArray.

You can find the documentation on `gsw-xarray.readthedocs.io <https://gsw-xarray.readthedocs.io/>`_.

Usage
-----
Simple usage
............

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

Using Pint
..........
   
We support (and convert the unit if necessary) the usage of pint.Quantities and the usage of xarray wrapped Quantities.
Support for pint requires the installation of two optional dependencies: ``pint`` and ``pint-xarray``.
If all the inputs to a gsw function are Quantities, the returned object will also be a Quantity belonging to the same UnitRegistry.

.. warning::

   Quantities must all belong to the same pint.UnitRegistry, a ValueError will be thrown if there are mixed registries.

.. warning::

   If one input is a Quantity, all inputs must be Quantities (and/or xarray wrapped Quantities), except for the `axis` and `interp_method` arguments.
   For mixed usage of Quantities and non Quantities, a ValueError will be thrown.

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

The usage of xarray wrapped Quantities is not required, you can use pint directly (though the ``pint-xarray`` dep still needs to be installed).

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

As gsw-xarray converts arguments to the proper unit when Quantities are used, we can e.g. use the temperature in Kelvin:

.. code:: python

   CT = ureg.Quantity(10, ureg.degC).to('kelvin')
   sigma0 = gsw.sigma0(SA=SA, CT=CT)
   print(sigma0)

Outputs

::

   26.824644457868317 kilogram / meter ** 3

.. note::
   If you do not wish to use the unit conversion ability, you need to pass dequantified Quantities
   (e.g. `da.pint.dequantify()` for pint-xarray or `arg.magnitude` for pint.Quantity).

.. warning::
   On the opposite, gsw-xarray will not check the units if non Quantity arguments are used.
   If you wish to use unit conversion, please pass quantified arguments (if your xarray.Dataset /
   xarray.DataArray has the 'units' attribute, you can use `da.pint.quantify()`)

.. note::
   We recommend that you use the `cf-xarray <https://cf-xarray.readthedocs.io/en/latest/units.html>`_ registry for units,
   as it implements geophysical units as `degree_north`, `degrees_north`, etc.
   gsw-xarray internally uses `degree_north` and `degree_east` for latitude and longitude unit names.
   If they are not found in the unit registry, they will be replaced by `degree`.

   The function `gsw.SP_from_SK` uses part per thousand for SK. 'ppt' is already used for picopint,
   so the expected unit is replaced by '1'.


Xarray accessor
...............

gsw-xarray provides a new accessor for xarray, that allows to call the gsw **functions** directly on a dataset:

.. code:: python

   ds.gsw.sigma0(CT="CT", SA="SA")
   # or
   ds.gsw.sigma0(CT=ds.CT, SA=ds.SA)
   # or even, if CT and SA have the proper standard names
   ds.gsw.sigma0()

Any type of mixte usage with dataArrays, numbers, strings, or autoparse with standard names is possible.

If all arguments are present in the dataset with the proper standard name, it is possible to use the accessor with brackets, as if it was a dictionary

.. code:: python

   ds.gsw["sigma0"]
   # Or if you want to get a list of multiple variables
   ds.gsw[["sigma0", "alpha"]]

If the dataset contains multiple variables with same standard name (e.g. practical salinity from bottle or CTD), you can set an option to tell gsw_xarray which variable to get:

.. code:: python

   # Globally
   gsw_xarray.set_cf_name_preference(standard_name="variable_in_dataset")
   # Or in a context, e.g.
   with gsw_xarray.set_non_cf_name(sea_water_pressure="pres_adjusted"):
       # write code here
       pass
   
If you wish to use the accessor with automatic detection of arguments, but for a function whose arguments do not have a standard name, it is possible. You need to set an option in gsw-xarray, either in a context or globally

.. code:: python

   # Globally
   gsw_xarray.set_non_cf_name(argument="argument_name_in_dataset")
   # Or in a context, e.g.
   with gsw_xarray.set_non_cf_name(Rt="Rt_in_ds"):
       ds.gsw.SP_salinometer(t=0)

In this 2nd case, the function ``gsw.SP_salinometer`` take the argument ``Rt`` which has no standard name.

When using user set options, the order of priority to automatically get variables is: 1) variables set by ``gsw_xarray.set_cf_name_preference``, 2) variables with standard name (internal mapping), and 3) variables set by ``gsw_xarray.set_non_cf_name``.
   
Installation
------------
Pip
...

.. code:: bash

    pip install gsw-xarray


Conda
.....

Inside a conda environment:  ``conda install -c conda-forge gsw-xarray``.


Citation
--------

If you use gsw-xarray, please cite the reference paper for the upstream gsw library:  McDougall, T.J. and P.M. Barker, 2011: Getting started with TEOS-10 and the Gibbs Seawater (GSW) Oceanographic Toolbox, 28pp., SCOR/IAPSO WG127, ISBN 978-0-646-55621-5

.. code-block:: bibtex

    @book{mcdougall2011getting,
      author = {McDougall, T. J. and Barker, P. M.},
      title = {Getting Started with TEOS-10 and the Gibbs Seawater (GSW) Oceanographic Toolbox},
      year = {2011},
      pages = {28},
      publisher = {SCOR/IAPSO WG127},
      isbn = {978-0-646-55621-5}
    }

You can also cite gsw-xarray by using the zenodo DOI |zenodo|.

Contributor guide
-----------------

All contributions, bug reports, bug fixes, documentation improvements,
enhancements, and ideas are welcome.
If you notice a bug or are missing a feature, fell free
to open an issue in the `GitHub issues page <https://github.com/DocOtak/gsw-xarray/issues>`_.

In order to contribute to gsw-xarray, please fork the repository and
submit a pull request. A good step by step tutorial for starting with git can be found in the
`xarray contributor guide <https://xarray.pydata.org/en/stable/contributing.html#working-with-the-code>`_.
A main difference is that we do not use conda as python environment, but uv.

Set up the environment
......................

You will first need to `install uv <https://docs.astral.sh/uv/getting-started/installation/>`_.
Then go to your local clone of gsw-xarray and launch installation:

.. code:: bash

   cd /path/to/your/gsw-xarray
   uv sync --all-groups

If desired, you can then activate the environment manually:

.. code:: bash

   source .venv/bin/activate

You can check that the tests pass locally:

.. code:: bash

   uv run pytest gsw_xarray/tests

You can install `pre-commit <https://pre-commit.com/#install>`_ to run the linting
automatically at each commit.
   
Release (for maintainers only)
..............................

TODO...
