import pytest

from .._function_utils import args_and_kwargs_to_args, get_args_names


def func(a, b, c=2, d=3):
    return


def test_args_and_kwargs_to_args():
    ref = {"a": 0, "b": 1, "c": 2, "d": 3}
    args = [0, 1]
    kwargs = dict(c=2, d=3)
    assert args_and_kwargs_to_args(func, args, kwargs) == ref
    args = [0, 1, 2, 3]
    kwargs = dict()
    assert args_and_kwargs_to_args(func, args, kwargs) == ref
    args = [0]
    kwargs = dict(c=2, d=3, b=1)
    assert args_and_kwargs_to_args(func, args, kwargs) == ref


@pytest.mark.parametrize("n", range(4 + 1))
def test_get_args_names(n):
    ref = ["a", "b", "c", "d"]
    args = list(range(n))
    assert get_args_names(func, args) == ref[:n]
