
from itertools import *

def iter_groupby(iterator, fun):
    result = []
    tmp = []
    for item in iterator:
        if len(tmp) == 0:
            tmp.append(item)
            continue
        if fun(tmp[-1], item):
            tmp.append(item)
        else:
            result.append(tmp)
            tmp = [item]
    if len(tmp) > 0:
        result.append(tmp)
    return result

def iter_group(iterator, num):
    result = []
    tmp = []
    for i, item in enumerate(iterator, start=1):
        if i % num == 0:
            tmp.append(item)
            result.append(tmp)
            tmp = []
        else:
            tmp.append(item)
    if len(tmp) > 0:
        result.append(tmp)
    return result


def iter_split(iterator, fun):
    result = []
    tmp = []
    for l in iterator:
        if not fun(l):
            tmp.append(l)
        else:
            result.append(tmp)
            tmp = []
    if len(tmp) > 0:
        result.append(tmp)
    return result

def parse_int(s):
    return int(s.strip())
