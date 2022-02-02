gsw_xarray: Wrapper for gsw that adds CF attributes
===================================================

gsw_xarray is a wrapper for `gsw python <https://github.com/TEOS-10/GSW-python>`_
that will add CF attributes to xarray.DataArray outputs.

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

   {'standard_name': 'sea_water_sigma_t', 'units': 'kg m-3'}

Installation
------------
Pip
...

.. code:: bash

    pip install gsw_xarray


Conda
.....

Activate your conda environment, and then use ``pip install gsw_xarray``.

Pipenv
......

Inside a pipenv environment: ``pipenv install gsw_xarray``.

Contributor guide
-----------------
