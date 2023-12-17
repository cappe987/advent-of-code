import sys
sys.path.append('../')
from aoclib import *
from heapq import *

data = open("example.txt").readlines()
data = open("example2.txt").readlines()
data = open("input.txt").readlines()

def move(pos, d):
    return pos[0]+d[0], pos[1]+d[1]

def p1_cond(d, cd):
    return d == cd[-1] and len(cd) == 3

def p2_cond(d, cd):
    return (d == cd[-1] and len(cd) == 10) or (d != cd[-1] and len(cd) < 4)

def solve(grid, part2):
    start = (0,0)
    goal = (len(grid)-1,len(grid[0])-1)
    pq = []
    visited = set()

    dirs = {">": (1, 0), "v": (0, 1), "^": (0, -1), "<": (-1, 0)}
    opposite = {"<": ">", ">": "<", "v": "^", "^": "v"}

    pq = [(0, ">", start, [start]), (0, "v", start, [start])]

    while len(pq) > 0:
        ch, cd, cp, path = heappop(pq)

        if (cp, cd) in visited:
            continue
        visited.add((cp, cd))
        for d in dirs:
            np = move(cp, dirs[d])
            if (not in_range_grid(grid, np[0], np[1])
                or (not part2 and p1_cond(d, cd))
                or (part2 and p2_cond(d, cd))
                or cd[-1] == opposite[d]):
               continue
            if d == cd[-1]:
                nd = cd + d
            else:
                nd = d

            if (np, nd) in visited:
                continue

            nh = ch + grid[np[0]][np[1]]
            if np == goal and (not part2 or d == cd[-1] and len(cd) >= 4):
                return nh
            heappush(pq, (nh, nd, np, path+[np]))

grid = [list(map(int, x.strip())) for x in data]
print(f"Part 1: {solve(grid, False)}")
print(f"Part 2: {solve(grid, True)}")
