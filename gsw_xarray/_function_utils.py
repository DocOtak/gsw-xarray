from inspect import signature


def args_and_kwargs_to_kwargs(func, args, kwargs, add_defaults):
    s = signature(func)
    bound_args = s.bind(*args, **kwargs)
    if add_defaults:
        bound_args.apply_defaults()
    all_kwargs = bound_args.arguments
    return all_kwargs
