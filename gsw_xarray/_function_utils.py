from inspect import signature


def args_and_kwargs_to_kwargs(func, args, kwargs, add_defaults):
    s = signature(func)
    # Use s.bind_partial and not s.bind to allow for missing args
    bound_args = s.bind_partial(*args, **kwargs)
    if add_defaults:
        bound_args.apply_defaults()
    all_kwargs = bound_args.arguments
    return all_kwargs


def parameters_as_set(func):
    """
    Return a set with the names of the parameters of *func*
    """
    s = signature(func)
    p = s.parameters
    return set(p.keys())
