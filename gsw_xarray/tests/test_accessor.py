"""
Testing use of dataset
"""

import pytest
import xarray as xr

import gsw_xarray


def test_use_only_dataset_call(ds):
    """Use accessor"""
    sigma0_da = gsw_xarray.sigma0(SA=ds.SA, CT=ds.CT)
    sigma0_ds = ds.gsw.sigma0()
    xr.testing.assert_identical(sigma0_ds, sigma0_da)


def test_use_only_dataset_getitem(ds):
    """Use getitem"""
    sigma0_da = gsw_xarray.sigma0(SA=ds.SA, CT=ds.CT)
    sigma0_ds = ds.gsw["sigma0"]
    xr.testing.assert_identical(sigma0_ds, sigma0_da)


def test_use_only_dataset_call_pint(ds_pint):
    """Use accessor and pint"""
    pytest.importorskip("pint_xarray")
    sigma0_da = gsw_xarray.sigma0(SA=ds_pint.SA, CT=ds_pint.CT)
    sigma0_ds = ds_pint.gsw.sigma0()
    xr.testing.assert_identical(sigma0_ds, sigma0_da)


def test_use_only_dataset_getitem_pint(ds_pint):
    """Use getitem and pint"""
    pytest.importorskip("pint_xarray")
    sigma0_da = gsw_xarray.sigma0(SA=ds_pint.SA, CT=ds_pint.CT)
    sigma0_ds = ds_pint.gsw["sigma0"]
    xr.testing.assert_identical(sigma0_ds, sigma0_da)


def test_use_only_dataset_getitem_list(ds):
    """Use getitem with a list"""
    out = ds.gsw[["sigma0", "sigma1"]]
    assert isinstance(out, xr.Dataset)


def test_use_partial_dataset(ds):
    """Use accessor + some strings / DataArrays"""
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


def test_missing_argument_with_standard_name(ds):
    """If it misses an argument should raise a TypeError"""
    with pytest.raises(TypeError):
        ds.gsw.SA_from_SP(p=0, lon=0, lat=0)


def test_multiple_standard_names_for_same_argument(ds):
    """Test for practical salinity that has multiple standard names"""
    ds["psal"] = ds.SA
    ds["psal"].attrs["standard_name"] = "sea_water_practical_salinity"
    ds.gsw.SA_from_SP(p=0, lon=0, lat=0)
    # However ARGO data still have the old standard name sea_water_salinity
    ds["psal"].attrs["standard_name"] = "sea_water_salinity"
    ds.gsw.SA_from_SP(p=0, lon=0, lat=0)


def test_multiple_variables_with_same_standard_names(ds):
    """lot of tests with options for standard names and errors that must be raised"""
    ds["sal"] = ds.SA
    ds["sal"].attrs["standard_name"] = "sea_water_salinity"
    ds["psal"] = ds.SA
    ds["psal"].attrs["standard_name"] = "sea_water_practical_salinity"
    ds["psal2"] = ds.SA
    ds["psal2"].attrs["standard_name"] = "sea_water_practical_salinity"
    ds["lon"] = 0
    ds["lon"].attrs["standard_name"] = "longitude"
    ds["lon2"] = 0
    ds["lon2"].attrs["standard_name"] = "longitude"
    with gsw_xarray.set_cf_name_preference(sea_water_practical_salinity="psal2"):
        ds.gsw.SA_from_SP(p=0, lon=0, lat=0)
    with gsw_xarray.set_cf_name_preference(longitude="lon"):
        ds.gsw.SA_from_SP(SP=0, p=0, lat=0)
    with pytest.raises(KeyError):
        ds.gsw.SA_from_SP(p=0, SP=0, lat=0)
    with pytest.raises(KeyError):
        ds.gsw.SA_from_SP(p=0, lon=0, lat=0)
    ds = ds.drop_vars("psal")
    with pytest.raises(TypeError):
        ds.gsw.SA_from_SP(p=0, lon=0, lat=0)


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
    """If there is no standard name and the argument is missing, must raise TypeError"""
    with pytest.raises(TypeError):
        ds.gsw.SP_salinometer(t=0)


def test_missing_standard_name_setting_option(ds):
    """Test option set_non_cf_name"""
    ds["Rt_in_ds"] = 0
    with gsw_xarray.set_options(non_cf_name={"Rt": "Rt_in_ds"}):
        ds.gsw.SP_salinometer(t=0)
    # Or
    with gsw_xarray.set_non_cf_name(Rt="Rt_in_ds"):
        ds.gsw.SP_salinometer(t=0)


def test_missing_standard_name_and_option_multiple_standard_names(ds):
    """Test option set_non_cf_name along with"""
    ds["Rt_in_ds"] = 0
    ds["t"] = ds.CT
    ds["t"].attrs["standard_name"] = "sea_water_temperature"
    ds["t2"] = ds.CT
    ds["t2"].attrs["standard_name"] = "sea_water_temperature"
    with gsw_xarray.set_options(non_cf_name={"Rt": "Rt_in_ds"}):
        with gsw_xarray.set_cf_name_preference(sea_water_temperature="t2"):
            ds.gsw.SP_salinometer()


def test_no_access_to_modules(ds):
    """The accessor does not provide access to the gsw modules"""
    with pytest.raises(AttributeError):
        ds.gsw["density"]


def test_no_access_to_unexisting_func(ds):
    """Raise attribute error if we try to access something not existing in gsw upstream"""
    with pytest.raises(AttributeError):
        ds.gsw["does_not_exist"]
