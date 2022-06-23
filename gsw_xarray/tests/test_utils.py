import pytest

from .._function_utils import args_and_kwargs_to_kwargs


def func(a, b, c=2, d=3):
    return


def test_args_and_kwargs_to_kwargs():
    ref = {"a": 0, "b": 1, "c": 2, "d": 3}
    args = [0, 1]
    kwargs = dict(c=2, d=3)
    assert args_and_kwargs_to_kwargs(func, args, kwargs, add_defaults=True) == ref
    args = [0, 1, 2, 3]
    kwargs = dict()
    assert args_and_kwargs_to_kwargs(func, args, kwargs, add_defaults=True) == ref
    args = [0]
    kwargs = dict(c=2, d=3, b=1)
    assert args_and_kwargs_to_kwargs(func, args, kwargs, add_defaults=True) == ref
