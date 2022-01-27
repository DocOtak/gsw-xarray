__version__ = "0.1.0"

import gsw
from ._core import _wrapped_funcs

# See PEP 562
def __getattr__(name):
    try:
        return _wrapped_funcs[name]
    except KeyError:
        try:
            return getattr(gsw, name)
        except AttributeError as error:
            raise AttributeError(
                f"module {__name__} has no attribute {name}"
            ) from error

def __dir__():
    return list(sorted(set([*_wrapped_funcs.keys(), *dir(gsw)])))
