from inspect import signature

def args_and_kwargs_to_kwargs(func, args, kwargs):
    s = signature(func)
    bound_args = s.bind(*args, **kwargs)
    bound_args.apply_defaults()
    all_kwargs = bound_args.arguments
    return all_kwargs
