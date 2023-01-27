import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("example2.txt").readlines()
data = open("input.txt").readlines()

def move(d,y,x):
    if d == "R": return (y,x+1)
    if d == "L": return (y,x-1)
    if d == "U": return (y-1,x)
    if d == "D": return (y+1,x)

def neigh(y,x):
    for _y in range(y-1,y+2):
        for _x in range(x-1,x+2):
            yield (_y, _x)

def dir(y,x):
    y = 1 if y < 0 else -1 if y > 0 else 0
    x = 1 if x < 0 else -1 if x > 0 else 0
    return y,x

def move_towards(to, fr):
    mv = dir(*(fr[0]-to[0],fr[1]-to[1]))
    return fr[0]+mv[0], fr[1]+mv[1]

def solve(data, knotcount):
    knots = [(0,0) for _ in range(knotcount)]
    visited = [(0,0)]
    for d, n in map(lambda x: x.strip().split(), data):
        for i in range(int(n)):
            knots[0] = move(d, knots[0][0], knots[0][1])
            for k, knot in enumerate(knots[1:], start=1):
                if knot not in neigh(knots[k-1][0], knots[k-1][1]):
                    knots[k] = move_towards(knots[k-1], knot)
                    if k == knotcount-1:
                        visited.append(knots[k])
    return len(set(visited))

print(f"Part 1: {solve(data, 2)}")
print(f"Part 2: {solve(data, 10)}")
