"""
Functions that return tuples must have tuples
(with the same length) as attributes and names
"""
import pytest
from inspect import signature, _empty

from .test_imports import gsw_base

from gsw_xarray._names import _names
from gsw_xarray._attributes import _func_attrs
import gsw


@pytest.mark.parametrize("func_name", gsw_base)
def test_(func_name):
    if func_name in ["indexer", "match_args_return", "pchip_interp"]:
        # Internal gsw cookery or non wrapped functions
        return
    f = getattr(gsw, func_name)
    n_args = len(signature(f).parameters)
    p = signature(f).parameters
    n_args = len([i for i in p.keys() if p[i].default is _empty])
    if "axis" in p.keys():
        # needs >= 2 data
        data = [1, 2]
    else:
        data = [1]
    print(n_args)
    res = f(
        *[
            data,
        ]
        * n_args
    )
    if isinstance(res, tuple):
        assert len(res) == len(_names[func_name])
        assert len(_names[func_name]) == len(_func_attrs[func_name])
    else:
        assert isinstance(_names[func_name], str)
        assert isinstance(_func_attrs[func_name], dict)
