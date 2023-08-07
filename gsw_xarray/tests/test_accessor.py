"""
Testing use of dataset
"""
import pytest
import gsw
import xarray as xr
import gsw_xarray

from .test_imports import gsw_base


def test_use_only_dataset_call(ds):
    """Give dataset as argument"""
    sigma0_da = gsw_xarray.sigma0(SA=ds.SA, CT=ds.CT)
    sigma0_ds = ds.gsw.sigma0()
    xr.testing.assert_identical(sigma0_ds, sigma0_da)


def test_use_only_dataset_getitem(ds):
    """Give dataset as argument"""
    sigma0_da = gsw_xarray.sigma0(SA=ds.SA, CT=ds.CT)
    sigma0_ds = ds.gsw["sigma0"]
    xr.testing.assert_identical(sigma0_ds, sigma0_da)


def test_use_only_dataset_getitem_list(ds):
    """Give dataset as argument"""
    out = ds.gsw[["sigma0", "sigma1"]]
    assert isinstance(out, xr.Dataset)


def test_use_partial_dataset(ds):
    """Give dataset as argument + some dataarrays"""
    sigma0_da = ds.gsw.sigma0(SA=ds.SA, CT=ds.CT)
    sigma0_ds = ds.gsw.sigma0(CT="CT")
    xr.testing.assert_identical(sigma0_ds, sigma0_da)
    # The following case must also work
    ds["SA2"] = ds["SA"].copy(deep=True)
    sigma0_ds = ds.gsw.sigma0(ds.SA)
    xr.testing.assert_identical(sigma0_ds, sigma0_da)
    # Must raise an error (multiple values for SA)
    with pytest.raises(KeyError):
        ds.gsw.sigma0()


def test_argument_t_ice(ds):
    """Test that for ice function, t is sea_ice_temperature"""
    ds["t"] = ds.CT
    ds["t"].attrs["standard_name"] = "sea_ice_temperature"
    ds.gsw.cp_ice(p=0)


def test_argument_t_seawater(ds):
    """Test that for sea water function, t is sea_water_temperature"""
    ds["t"] = ds.CT
    ds["t"].attrs["standard_name"] = "sea_water_temperature"
    ds.gsw.rho_t_exact(p=0)


def test_missing_standard_name(ds):
    """Give dataset as argument"""
    with pytest.raises(TypeError):
        ds.gsw.SP_salinometer(t=0)


def test_missing_standard_name_setting_option(ds):
    """Give dataset as argument"""
    ds["Rt_in_ds"] = 0
    with gsw_xarray.set_options(non_cf_name={"Rt": "Rt_in_ds"}):
        ds.gsw.SP_salinometer(t=0)
    # Or
    with gsw_xarray.set_non_cf_name(Rt="Rt_in_ds"):
        ds.gsw.SP_salinometer(t=0)
