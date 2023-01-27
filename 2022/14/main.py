import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def walk_points(a,b):
    if a[0] == b[0]:
        y = a[0]
        for x in range(min(a[1],b[1]), max(a[1],b[1])+1):
            yield (y,x)
    elif a[1] == b[1]:
        x = a[1]
        for y in range(min(a[0],b[0]), max(a[0],b[0])+1):
            yield (y,x)
    else: 
        print("Unexpected")

def solve(walls, part1):
    lowest = max(map(lambda x:x[0], walls))
    floor = lowest + 2
    sand = set()
    s = (0,500)
    while s[0] <= lowest if part1 else (0,500) not in sand:
        s = (0,500)
        while s[0] <= lowest if part1 else True:
            if not part1 and s[0] == floor-1:
                sand.add(s)
                break
            moved = False
            for p in [(s[0]+1, s[1]), (s[0]+1, s[1]-1), (s[0]+1, s[1]+1)]:
                if p not in walls and p not in sand:
                    s = p
                    moved = True
                    break
            if not moved:
                sand.add(s) 
                break
    return len(sand)

walls = set()
for line in data:
    points = line.strip().split(" -> ")
    points = list(map(lambda x: list(map(int, x.split(','))), points))
    for i in range(len(points)-1):
        for p in walk_points(points[i], points[i+1]):
            walls.add((p[1], p[0]))

print(solve(walls, True))
print(solve(walls, False))
