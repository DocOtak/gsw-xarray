import pytest

import xarray as xr
import numpy as np


@pytest.fixture
def ds():
    ds = xr.Dataset()
    id = np.arange(3)
    ds["id"] = xr.DataArray(id, coords={"id": id})
    ds["CT"] = ds["id"] * 10
    ds["CT"].attrs = {"standard_name": "sea_water_conservative_temperature"}
    ds["SA"] = ds["id"] * 0.1 + 34
    ds["SA"].attrs = {"standard_name": "sea_water_absolute_salinity"}
    return ds


@pytest.fixture(scope="session")
def ureg():
    pint = pytest.importorskip("pint")
    return pint.UnitRegistry()
