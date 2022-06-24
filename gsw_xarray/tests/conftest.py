import pytest

import xarray as xr
import numpy as np


@pytest.fixture
def ds():
    ds = xr.Dataset()
    id = np.arange(3)
    ds["id"] = xr.DataArray(id, coords={"id": id})
    ds["CT"] = ds["id"] * 1
    ds["CT"].attrs = {
        "standard_name": "sea_water_conservative_temperature",
        "units": "degC",
    }
    ds["SA"] = ds["id"] * 0.1 + 34
    ds["SA"].attrs = {"standard_name": "sea_water_absolute_salinity", "units": "g/kg"}
    ds["p"] = ds["id"] * 10
    ds["p"].attrs = {"standard_name": "sea_water_pressure", "units": "dbar"}
    return ds


@pytest.fixture(scope="session")
def ureg():
    pint_xarray = pytest.importorskip("pint_xarray")
    from pint_xarray import unit_registry as ureg

    return ureg


@pytest.fixture
def ds_pint(ds, ureg):
    pytest.importorskip("pint_xarray")

    return ds.pint.quantify()


@pytest.fixture
def S(ureg):
    return 35 * ureg("g / kg")


@pytest.fixture
def T(ureg):
    return ureg.Quantity(1, ureg.degC)
