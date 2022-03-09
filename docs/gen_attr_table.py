from gsw_xarray._names import _names
from gsw_xarray._attributes import _func_attrs


list_table = ""


for name, result_name in _names.items():
    list_table += f"{name}\n{'-' * len(name)}\n"
    if isinstance(result_name, tuple):
        list_table += f"Has {len(result_name)} outputs\n\n"
        for i, result in enumerate(result_name):
            list_table += f"**{result}**\n\n"
            list_table += f"* standard_name: {_func_attrs[name][i].get('standard_name', '')}\n"
            list_table += f"* units: {_func_attrs[name][i].get('units', '')}\n\n"

    else:
        list_table += "Has 1 output\n\n"
        list_table += f"**{result_name}**\n\n"
        list_table += f"* standard_name: {_func_attrs[name].get('standard_name', '')}\n"
        list_table += f"* units: {_func_attrs[name].get('units', '')}\n\n"
    list_table += "\n"



print(list_table)