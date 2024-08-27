import inspect
from pprint import pprint


def introspection_info(obj):
    info = {}
    atr =[]
    method = []
    info['type'] = type(obj)
    for i in dir(obj):
        if i.startswith("__") or i.startswith("_"):
            atr.append(i)
            info['attributes'] = atr
        else:
            method.append(i)
            info['methods'] = method
    info['module'] = inspect.getmodule(introspection_info)
    return info



number_info = introspection_info(23)
pprint(number_info)