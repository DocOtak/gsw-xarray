from gsw_xarray import __version__
import gsw_xarray as gsw
import xarray as xr
import numpy as np
import pytest


def test_version():
    assert __version__ == "0.2.1"


def test_func_standard(ds):
    """Basic test"""
    sigma0 = gsw.sigma0(SA=ds.SA, CT=ds.CT)
    assert sigma0.attrs["standard_name"] == "sea_water_sigma_t"
    assert sigma0.name == "sigma0"
    assert sigma0.attrs["units"] == "kg/m^3"


def test_func_return_tuple(ds):
    (CT_SA, CT_pt) = gsw.CT_first_derivatives(ds.SA, 1)
    assert CT_SA.name == "CT_SA"
    assert CT_SA.attrs["units"] == "K/(g/kg)"


def test_func_return_tuple_ndarray(ds):
    (CT_SA, CT_pt) = gsw.CT_first_derivatives(ds.SA.data, 1)
    assert isinstance(CT_SA, np.ndarray)
    assert isinstance(CT_pt, np.ndarray)


@pytest.mark.parametrize("gsdh", [0, 1, None])
@pytest.mark.parametrize("ssg", [0, 1, None])
@pytest.mark.parametrize(
    "use_kw",
    [
        [
            False,
        ]
        * (4 - i)
        + [
            True,
        ]
        * i
        for i in range(5)
    ],
)
def test_check_func(gsdh, ssg, use_kw):
    ds = xr.Dataset()
    ds["p"] = xr.DataArray([0, 1, 2])
    ds["lat"] = xr.DataArray([40, 41, 21])
    args = []
    kwargs = {}
    if use_kw[0]:
        kwargs["p"] = ds["p"]
    else:
        args.append(ds["p"])
    if use_kw[1]:
        kwargs["lat"] = ds["lat"]
    else:
        args.append(ds["lat"])
    if gsdh is not None:
        if use_kw[2]:
            kwargs["geo_strf_dyn_height"] = gsdh
        else:
            args.append(gsdh)
    if ssg is not None:
        if use_kw[3]:
            kwargs["sea_surface_geopotential"] = ssg
        else:
            args.append(ssg)
    z = gsw.z_from_p(*args, **kwargs)
    if gsdh not in (0, None) or ssg not in (0, None):
        assert "standard_name" not in z.attrs.keys()
    else:
        assert "standard_name" in z.attrs.keys()
