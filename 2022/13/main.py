import sys
sys.path.append('../')
from aoclib import *
from functools import cmp_to_key

data = open("example.txt").readlines()
data = open("input.txt").readlines()

data = [eval(line.strip()) for line in data if line != "\n"]

def compare(a, b):
    if type(a) == int and type(b) == int:
        return b - a
    _a = [a] if type(a) == int else a
    _b = [b] if type(b) == int else b

    i = 0
    while i < len(_a) and i < len(_b):
        res = compare(_a[i], _b[i])
        if res != 0:
            return res
        i += 1

    return len(_b) - len(_a)

correct = [i+1 for i,g in enumerate(iter_group(data, 2)) if compare(g[0],g[1]) > 0]
print(f'Part 1: {sum(correct)}')

data.extend([[[2]],[[6]]])
ordered = sorted(data, key=cmp_to_key(compare), reverse=True)
answer = (ordered.index([[2]])+1) * (ordered.index([[6]])+1)
print(f'Part 2: {answer}')
