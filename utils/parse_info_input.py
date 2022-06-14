from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString, Tag

import gsw
from types import FunctionType

from functools import reduce

url = "https://www.teos-10.org/pubs/gsw/html/gsw_{}.html"

repls = ("deg C", "degC"), ("unitless", "1"), ("degrees of rotation", "arcdeg")


def parse_info(func_name, url=url):
    soup = BeautifulSoup(urlopen(url.format(func_name)), features="html.parser")
    for header in soup.find_all("h2"):
        if header.text != "INPUT:":
            continue
        nextNode = header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag):
                if nextNode.name == "h2":
                    break
                txt = nextNode.get_text(strip=True).strip()
                args = [i for i in txt.split('\n') if '=' in i]
                return [(i.split("=")[0].strip(), reduce(lambda a, kv: a.replace(*kv), repls, i.split("[")[1].split("]")[0].strip())) for i in args]
    return []


def print_dict_attrs():
    all_gsw_function = [
        i
        for i in dir(gsw)
        if (isinstance(getattr(gsw, i), FunctionType) and not i.startswith("_"))
    ]
    args_all = {}
    for func in all_gsw_function[:]:
        try:
            args = parse_info(func)
        except:
            args = []
        args_all[func] = args
    print(args_all)
    print('\n\n********************\n\n')
    get_units_per_arg(args_all)

def get_units_per_arg(args_all):
    units = {}
    for f in args_all.keys():
        args = args_all[f]
        for a in args:
            if a[0] == 'h':
                print(f, a)
            if a[0] in units.keys():
                if a[1] not in units[a[0]]:
                    units[a[0]].append(a[1])
            else:
                units[a[0]] = [a[1]]
    print(units)

if __name__ == '__main__':
    print_dict_attrs()
