import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def solve(corners):
    area = 0
    outer = 1
    for i in range(len(corners)):
        y1,x1 = corners[i]
        y2,x2 = corners[(i+1) % len(corners)]
        # tot += (corners[i+1][1] + corners[i][1]) * (corners[i+1][0] - corners[i][0])
        area += (x1*y2) - (y1*x2)
        outer += manhattan_distance((x1, y1), (x2, y2))

    return abs(area)//2 + outer//2 + 1

def new_pos(cp, d, n):
    if d == "R":
        return cp[0],cp[1]+n
    elif d == "L":
        return cp[0],cp[1]-n
    elif d == "D":
        return cp[0]+n,cp[1]
    elif d == "U":
        return cp[0]-n,cp[1]

direction = ["R", "D", "L", "U"]
corners = [(0,0)]
corners_p2 = [(0,0)]
for line in data:
    d, n, rem = line.split()
    n = int(n)
    cp = corners[-1]
    corners.append(new_pos(cp, d, n))
    cp = corners_p2[-1]
    d = direction[int(rem[-2])]
    n = int(rem[2:-2], 16)
    corners_p2.append(new_pos(cp, d, n))

print(f"Part 1: {solve(corners)}")
print(f"Part 2: {solve(corners_p2)}")
