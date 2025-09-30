"""
Functions that return tuples must have tuples
(with the same length) as attributes and names
"""

import warnings
from inspect import _empty, signature

import gsw
import pytest

from gsw_xarray._attributes import _func_attrs
from gsw_xarray._names import _names

from .test_imports import gsw_base


@pytest.mark.parametrize("func_name", gsw_base)
def test_(func_name):
    if func_name in [
        "indexer",
        "match_args_return",
        "pchip_interp",
        "gibbs",
        "gibbs_ice",
    ]:
        # Internal gsw cookery or non wrapped functions
        return
    if func_name not in _names:
        warnings.warn(f"Function *{func_name}* has not been wrapped yet")
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
