from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString, Tag

import gsw
from types import FunctionType

url = 'https://www.teos-10.org/pubs/gsw/html/gsw_{}.html'

def parse_info(func_name, url=url):
    soup = BeautifulSoup(urlopen(url.format(func_name)), features="html.parser")
    for header in soup.find_all('h2'):
        if header.text != 'OUTPUT:': 
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
    name = txt.split('=')[0].strip()
    unit = txt.split('[')[1].split(']')[0].strip()
    return (name, unit)

def print_dict_attrs():    
    all_gsw_function = [i for i in dir(gsw) if (isinstance(getattr(gsw, i), FunctionType) and not i.startswith('_'))]
    attrs = {}
    names = {}
    for func in all_gsw_function:
        try:
            name, unit = parse_info(func)
        except:
            name, unit = ('', '')
        names[func] = name
        attrs[func] = {'units':unit}
    print(attrs)
    print(names)
