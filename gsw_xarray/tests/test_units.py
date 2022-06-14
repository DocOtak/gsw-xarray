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


def test_xarray_quantity(ds_pint):
    pint_xarray = pytest.importorskip("pint_xarray")
    sigma0 = gsw_xarray.sigma0(SA=ds_pint.SA, CT=ds_pint.CT)
    assert sigma0.pint.units == pint_xarray.unit_registry("kg / m^3")


@pytest.mark.parametrize("SA_type", ["unit", "ds"])
@pytest.mark.parametrize("CT_type", ["unit", "ds"])
def test_xarray_quantity_or_ds(ds, ds_pint, SA_type, CT_type):
    """If at least 1 of the inputs is quantity, the result should be quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")
    if SA_type == "unit":
        SA = ds_pint.SA
    elif SA_type == "ds":
        SA = ds.SA

    if CT_type == "unit":
        CT = ds_pint.CT
    elif CT_type == "ds":
        CT = ds.CT

    sigma0 = gsw_xarray.sigma0(SA=SA, CT=CT)
    if SA_type == "unit" or CT_type == "unit":
        assert sigma0.pint.units == pint_xarray.unit_registry("kg / m^3")
    else:
        assert sigma0.pint.units is None
        assert sigma0.pint.quantify().pint.units == pint_xarray.unit_registry(
            "kg / m^3"
        )


def test_func_return_tuple_quantity(ds_pint):
    pint_xarray = pytest.importorskip("pint_xarray")
    (CT_SA, CT_pt) = gsw_xarray.CT_first_derivatives(ds_pint.SA, 1)
    assert CT_SA.pint.units == pint_xarray.unit_registry("K/(g/kg)")


def test_pint_quantity_xarray(ds, T):
    """If input is mixed between xr.DataArray and pint quantity it should return pint-xarray wrapped quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")

    sigma0 = gsw_xarray.sigma0(SA=ds.SA, CT=T)
    assert sigma0.pint.units == pint_xarray.unit_registry("kg / m^3")


def test_pint_quantity(S):
    """If input is pint quantity should return a quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")
    pint = pytest.importorskip("pint")

    CT = gsw_xarray.CT_from_pt(SA=S, pt=10)
    assert isinstance(CT, pint.Quantity)


def test_pint_quantity_tuple(S):
    """If input is pint quantity should return a quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")
    import pint

    (a, b) = gsw_xarray.CT_first_derivatives(S, pt=1)
    assert isinstance(a, pint.Quantity)
    assert isinstance(b, pint.Quantity)


def test_mixed_unit_regestiries():
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
    print("*****", sigma0_good_units, sigma0_bad_units)
    xr.testing.assert_equal(sigma0_good_units, sigma0_bad_units)


def test_pint_quantity_convert_args(ds_pint):
    pint_xarray = pytest.importorskip("pint_xarray")

    sigma0_good_units = gsw_xarray.sigma0(ds_pint.SA, ds_pint.CT)
    sigma0_bad_units = gsw_xarray.sigma0(
        ds_pint.SA.pint.to("mg / kg"), ds_pint.CT.pint.to("kelvin")
    )
    print("*****", sigma0_good_units, sigma0_bad_units)
    xr.testing.assert_equal(sigma0_good_units, sigma0_bad_units)


def test_pint_quantity_convert_kwargs_pint(S, T):
    pint_xarray = pytest.importorskip("pint_xarray")

    sigma0_good_units = gsw_xarray.sigma0(SA=S, CT=T)
    sigma0_bad_units = gsw_xarray.sigma0(SA=S.to("mg / kg"), CT=T.to("kelvin"))
    print("*****", sigma0_good_units, sigma0_bad_units)
    assert np.allclose(sigma0_good_units, sigma0_bad_units)


def test_pint_quantity_convert_args_pint(S, T):
    pint_xarray = pytest.importorskip("pint_xarray")

    sigma0_good_units = gsw_xarray.sigma0(S, T)
    sigma0_bad_units = gsw_xarray.sigma0(S.to("mg / kg"), T.to("kelvin"))
    print("*****", sigma0_good_units, sigma0_bad_units)
    assert np.allclose(sigma0_good_units, sigma0_bad_units)
