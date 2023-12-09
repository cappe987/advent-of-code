import sys
sys.path.append('../')
from aoclib import *
from functools import reduce

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def predict(xs):
    ls = []
    allzero = True
    for i in range(1, len(xs)):
        x = xs[i]-xs[i-1]
        if x != 0:
            allzero = False
        ls.append(x)

    if allzero:
        return (xs[0], xs[-1])
    start, end = predict(ls)
    return (xs[0] - start, xs[-1] + end)

data = map(lambda x: list(map(int, x.split())), data)
p2,p1 = reduce(lambda a,b: (a[0]+b[0], a[1]+b[1]), map(predict, data))
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
