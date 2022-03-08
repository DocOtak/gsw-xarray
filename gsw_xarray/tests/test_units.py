"""
Testing units with pint
"""
import pytest

from .test_imports import gsw_base
from gsw_xarray._attributes import _func_attrs

from pint import UnitRegistry

ureg = UnitRegistry()


@pytest.mark.parametrize("func_name", gsw_base)
def test_unit_pint(func_name):
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
