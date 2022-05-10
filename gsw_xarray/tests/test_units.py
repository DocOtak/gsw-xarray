"""
Testing units with pint and cf_units
"""
import pytest

import gsw_xarray

from .test_imports import gsw_base
from gsw_xarray._attributes import _func_attrs


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

@pytest.mark.parametrize("SA_type", ['unit', 'ds'])
@pytest.mark.parametrize("CT_type", ['unit', 'ds'])
def test_xarray_quantity_or_ds(ds, ds_pint, SA_type, CT_type):
    """If at least 1 of the inputs is quantity, the result should be quantity"""
    pint_xarray = pytest.importorskip("pint_xarray")
    if SA_type == 'unit':
        SA = ds_pint.SA
    elif SA_type == 'ds':
        SA = ds.SA
    
    if CT_type == 'unit':
        CT = ds_pint.CT
    elif CT_type == 'ds':
        CT = ds.CT
        
    sigma0 = gsw_xarray.sigma0(SA=SA, CT=CT)
    if SA_type == 'unit' or CT_type == 'unit':
        assert sigma0.pint.units == pint_xarray.unit_registry("kg / m^3")
    else:
        assert sigma0.pint.units is None
        assert sigma0.pint.quantify().pint.units == pint_xarray.unit_registry("kg / m^3")


def test_func_return_tuple_quantity(ds_pint):
    pint_xarray = pytest.importorskip("pint_xarray")
    (CT_SA, CT_pt) = gsw_xarray.CT_first_derivatives(ds_pint.SA, 1)
    assert CT_SA.pint.units == pint_xarray.unit_registry("K/(g/kg)")
