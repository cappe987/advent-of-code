import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def tilt(grid, direction):
    if direction == 'N':
        istart, iend, istep = (0, len(grid), 1)
        jstart, jend, jstep = (0, len(grid[0]), 1)
        move = (-1, 0)
    elif direction == 'E':
        istart, iend, istep = (0, len(grid), 1)
        jstart, jend, jstep = (len(grid[0])-1, -1, -1)
        move = (0, 1)
    elif direction == 'W':
        istart, iend, istep = (0, len(grid), 1)
        jstart, jend, jstep = (0, len(grid[0]), 1)
        move = (0, -1)
    elif direction == 'S':
        istart, iend, istep = (len(grid)-1, -1, -1)
        jstart, jend, jstep = (0, len(grid[0]), 1)
        move = (1, 0)

    for i in range(istart, iend, istep):
        for j in range(jstart, jend, jstep):
            if grid[i][j] == 'O':
                i2,j2 = (i+move[0],j+move[1])
                while in_range_grid(grid, i2, j2) and grid[i2][j2] == '.':
                    i2,j2 = (i2+move[0],j2+move[1])

                i2,j2 = (i2-move[0],j2-move[1])
                grid[i][j] = '.'
                grid[i2][j2] = 'O'

def score(grid):
    istart, iend, istep = (0, len(grid), 1)
    jstart, jend, jstep = (0, len(grid[0]), 1)
    score = 0
    for i in range(istart, iend, istep):
        for j in range(jstart, jend, jstep):
            if grid[i][j] == 'O':
                score += len(grid)-i

    return score

grid = [list(line.strip()) for line in data]
tilt(grid, "N")
print(f"Part 1: {score(grid)}")

grid = [list(line.strip()) for line in data]
grids = {}
for i in range(1000000000):
    for d in ["N", "W", "S", "E"]:
        tilt(grid, d)
    t = tuple([tuple(x) for x in grid])
    if t in grids:
        break
    grids[t] = i

t = tuple([tuple(x) for x in grid])
ti = grids[t]
cycle_length = i - ti
x = 1000000000-ti
in_cycle = x % cycle_length
idx = in_cycle + ti-1
for g,i in grids.items():
    if i == idx:
        print(f"Part 2: {score(g)}")
        break
