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
