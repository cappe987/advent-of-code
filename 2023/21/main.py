import sys
sys.path.append('../')
from aoclib import *
from math import floor

data = open("example.txt").readlines()
data = open("input.txt").readlines()

grid = [line.strip() for line in data]

def neighbours(i, j):
    return [(i-1,j), (i,j-1), (i,j+1), (i+1,j)]

def f(n, y0, y1, y2):
    a = (y2+y0-2*y1)/2
    b = y1-y0 -a
    c = y0
    return a*n**2 + b*n +c


steps = 26501365
period = 131
offset = steps % period

start = [(i,j) for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j] == 'S']
prev = set(start)
points = []
for step in range(1, steps+1):
    curr = set()
    for (i,j) in prev:
        for (i2,j2) in neighbours(i, j):
            i3,j3 = i2 % len(grid), j2 % len(grid[0])
            if grid[i3][j3] == '#':
                continue
            curr.add((i2,j2))

    if step == 64:
        print(f"Part 1: {len(curr)}")
    if step in [offset, offset + period, offset + period*2]:
        points.append(len(curr))
        if len(points) == 3:
            break
    prev = curr
        
res = floor(f(steps//period, points[0], points[1], points[2]))
print(f"Part 2: {res}")

