"""
Testing units with pint and cf_units
"""
import pytest
import numpy as np
import xarray as xr
import gsw
import gsw_xarray

from .test_imports import gsw_base
from gsw_xarray._attributes import _func_attrs
from gsw_xarray._arguments import input_units
from inspect import signature

##########
# Outputs
##########


@pytest.mark.parametrize("func_name", gsw_base)
def test_unit_pint(func_name, ureg):

    if func_name in ["indexer", "match_args_return", "pchip_interp"]:
        # Internal gsw cookery or non wrapped functions
        return
    if func_name == "geostrophic_velocity":
        pytest.xfail(
            'geostrophic_velocity outputs "degree_north" and "degree_east" that are not compatible with pint'
        )
    attrs = _func_attrs[func_name]
    if isinstance(attrs, dict):
        attrs = [
            attrs,
        ]
    for a in attrs:
        print(a["units"])
        ureg.Unit(a["units"])


@pytest.mark.parametrize("func_name", gsw_base)
def test_unit_cf_units(func_name):
    cf_units = pytest.importorskip("cf_units")
    if func_name in ["indexer", "match_args_return", "pchip_interp"]:
        # Internal gsw cookery or non wrapped functions
        return
    attrs = _func_attrs[func_name]
    if isinstance(attrs, dict):
        attrs = [
            attrs,
        ]
    for a in attrs:
        print(a["units"])
        cf_units.Unit(a["units"])


def test_xarray_quantity(ds_pint):
    pint_xarray = pytest.importorskip("pint_xarray")
    sigma0 = gsw_xarray.sigma0(SA=ds_pint.SA, CT=ds_pint.CT)
    assert sigma0.pint.units == pint_xarray.unit_registry("kg / m^3")


def test_func_return_tuple_quantity(ds_pint):
    pint_xarray = pytest.importorskip("pint_xarray")
    (CT_SA, CT_pt) = gsw_xarray.CT_first_derivatives(ds_pint.SA, ds_pint.CT)
    assert CT_SA.pint.units == pint_xarray.unit_registry("K/(g/kg)")


def test_output_falls_back_to_generic_unit(ds_pint):
    # We can't test geostrophic_velocity with xarray for now
    # see https://github.com/TEOS-10/GSW-Python/pull/96
    ureg = ds_pint.SA.pint.registry
    dyn_height = gsw_xarray.geo_strf_dyn_height(
        ds_pint.SA.data,
        ds_pint.CT.data,
        ds_pint.p.data,
        axis=ds_pint.p.get_axis_num("id"),
    )[1]
    dyn_height = np.ones((2,)) * dyn_height
    lon = ureg.Quantity([0, 15], "degree")
    lat = ureg.Quantity([10, 20], "degree")
    (vel, lon, lat) = gsw_xarray.geostrophic_velocity(dyn_height, lon, lat, axis=0)
    assert lon.units == ureg("degree")
    assert lat.units == ureg("degree")


##########
# Input
##########


@pytest.mark.parametrize("func_name", gsw_base)
def test_unit_of_arg(func_name, ureg):

    if func_name in ["indexer", "match_args_return", "pchip_interp"]:
        # Internal gsw cookery or non wrapped functions
        return
    func = getattr(gsw, func_name)
    s = signature(func)
    p = s.parameters
    for i in p:
        assert i in input_units.keys()


def test_ds_mixed_quantity_non_quantity(ds, ds_pint):
    """If at least 1 of the inputs is quantity, all inputs should be quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")

    with pytest.raises(ValueError):
        sigma0 = gsw_xarray.sigma0(SA=ds.SA, CT=ds_pint.CT)


def test_ds_mixed_quantity_non_quantity_axis_arg_None_arg(ds_pint):
    """Should not use dimension for None args, nor for the axis arg"""
    pint_xarray = pytest.importorskip("pint_xarray")

    gsw_xarray.Nsquared(SA=ds_pint.SA, CT=ds_pint.CT, p=ds_pint.p, axis=0, lat=None)


def test_pint_mixed_quantity_non_quantity(T):
    """If at least 1 of the inputs is quantity, all inputs should be quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")

    with pytest.raises(ValueError):
        sigma0 = gsw_xarray.sigma0(SA=35, CT=T)


def test_pint_quantity_xarray(ds_pint, T):
    """If input is mixed between pint-xarray and pint quantity it should return pint-xarray wrapped quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")

    sigma0 = gsw_xarray.sigma0(SA=ds_pint.SA, CT=T)
    assert sigma0.pint.units == pint_xarray.unit_registry("kg / m^3")


def test_pint_quantity(S, T):
    """If input is pint quantity should return a quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")
    pint = pytest.importorskip("pint")

    CT = gsw_xarray.CT_from_pt(SA=S, pt=T)
    assert isinstance(CT, pint.Quantity)


def test_pint_quantity_tuple(S, T):
    """If input is pint quantity should return a quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")
    import pint

    (a, b) = gsw_xarray.CT_first_derivatives(S, pt=T)
    assert isinstance(a, pint.Quantity)
    assert isinstance(b, pint.Quantity)


def test_mixed_unit_registries():
    """If input quantities are from different registries, it should fail"""
    pint_xarray = pytest.importorskip("pint_xarray")
    import pint

    ureg_a = pint.UnitRegistry()
    ureg_b = pint.UnitRegistry()
    with pytest.raises(ValueError):
        gsw_xarray.CT_first_derivatives(
            35 * ureg_a("g / kg"), pt=ureg_b.Quantity(1, ureg_b.degC)
        )


def test_pint_quantity_convert_kwargs(ds_pint):
    pint_xarray = pytest.importorskip("pint_xarray")

    sigma0_good_units = gsw_xarray.sigma0(SA=ds_pint.SA, CT=ds_pint.CT)
    sigma0_bad_units = gsw_xarray.sigma0(
        SA=ds_pint.SA.pint.to("mg / kg"), CT=ds_pint.CT.pint.to("kelvin")
    )
    xr.testing.assert_equal(sigma0_good_units, sigma0_bad_units)


def test_pint_quantity_convert_args(ds_pint):
    pint_xarray = pytest.importorskip("pint_xarray")

    sigma0_good_units = gsw_xarray.sigma0(ds_pint.SA, ds_pint.CT)
    sigma0_bad_units = gsw_xarray.sigma0(
        ds_pint.SA.pint.to("mg / kg"), ds_pint.CT.pint.to("kelvin")
    )
    xr.testing.assert_equal(sigma0_good_units, sigma0_bad_units)


def test_pint_quantity_convert_kwargs_pint(S, T):
    pint_xarray = pytest.importorskip("pint_xarray")

    sigma0_good_units = gsw_xarray.sigma0(SA=S, CT=T)
    sigma0_bad_units = gsw_xarray.sigma0(SA=S.to("mg / kg"), CT=T.to("kelvin"))
    assert np.allclose(sigma0_good_units, sigma0_bad_units)


def test_pint_quantity_convert_args_pint(S, T):
    pint_xarray = pytest.importorskip("pint_xarray")

    sigma0_good_units = gsw_xarray.sigma0(S, T)
    sigma0_bad_units = gsw_xarray.sigma0(S.to("mg / kg"), T.to("kelvin"))
    assert np.allclose(sigma0_good_units, sigma0_bad_units)
