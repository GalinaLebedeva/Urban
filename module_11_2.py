import inspect
from pprint import pprint


def introspection_info(obj):
    info = {}
    atr = []
    method = []
    info['type'] = type(obj)
    for i in dir(obj):
        if callable(getattr(obj,i)):
            method.append(i)
            info['attributes'] = atr
        else:
            atr.append(i)
            info['methods'] = method
    info['module'] = inspect.getmodule(introspection_info)
    return info


number_info = introspection_info(32)
pprint(number_info)
