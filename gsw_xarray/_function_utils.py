from inspect import signature

def args_and_kwargs_to_args(func, args, kwargs):
    
    s = signature(func)
    arg_names = list(s.parameters.keys())
    args_as_kwargs = {arg_names[i]: arg for i,arg in enumerate(args)}
    args_as_kwargs.update(kwargs)
    return args_as_kwargs

def get_args_names(func, args):
    s = signature(func)
    return list(s.bind_partial(*args).arguments.keys())
