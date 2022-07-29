"""
Testing use of dataset
"""
import pytest
import gsw
import gsw_xarray
import xarray as xr

from .test_imports import gsw_base


def test_use_only_dataset(ds):
    """Give dataset as argument"""
    sigma0_da = gsw_xarray.sigma0(SA=ds.SA, CT=ds.CT)
    sigma0_ds = gsw_xarray.sigma0(ds)
    xr.testing.assert_identical(sigma0_ds, sigma0_da)
    
def test_use_partial_dataset(ds):
    """Give dataset as argument + some dataarrays"""
    sigma0_da = gsw_xarray.sigma0(SA=ds.SA, CT=ds.CT)
    sigma0_ds = gsw_xarray.sigma0(ds, CT=ds.CT)
    xr.testing.assert_identical(sigma0_ds, sigma0_da)
    # The following case must also work
    ds.CT.attrs == {}
    sigma0_da = gsw_xarray.sigma0(SA=ds.SA, CT=ds.CT)
    sigma0_ds = gsw_xarray.sigma0(ds, CT=ds.CT)
    xr.testing.assert_identical(sigma0_ds, sigma0_da)
