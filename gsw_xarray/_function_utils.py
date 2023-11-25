from inspect import signature

from ._arguments import input_properties


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


def get_parameters_standard_name(func_name, parameters):
    """
    Return a dict with list of standard name(s) associated with parameters of func with func_name,
    when standard name(s) exist
    """
    standard_names = {}
    for p in parameters:
        if p == "t":
            if "ice" in func_name:
                standard_names[p] = ["sea_ice_temperature"]
            else:
                standard_names[p] = ["sea_water_temperature"]
        elif p == "p":
            if "ice" not in func_name:
                standard_names[p] = ["sea_water_pressure"]
        else:
            s = input_properties[p].get("standard_name")
            if s is None:
                continue
            if not isinstance(s, list):
                s = [s]
            standard_names[p] = s
    return standard_names
