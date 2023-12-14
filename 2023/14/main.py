import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def tilt(grid, direction):
    start, end, step = (0, len(grid), 1)
    if direction == 'N':
        move = (-1, 0)
    elif direction == 'W':
        move = (0, -1)
    else:
        start, end, step = (len(grid)-1, -1, -1)
        if direction == 'E':
            move = (0, 1)
        elif direction == 'S':
            move = (1, 0)

    for i in range(start, end, step):
        for j in range(start, end, step):
            if grid[i][j] == 'O':
                i2,j2 = (i+move[0],j+move[1])
                while in_range_grid(grid, i2, j2) and grid[i2][j2] == '.':
                    i2,j2 = (i2+move[0],j2+move[1])

                i2,j2 = (i2-move[0],j2-move[1])
                grid[i][j] = '.'
                grid[i2][j2] = 'O'

def score(grid):
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                score += len(grid)-i
    return score

# Part 1
grid = [list(line.strip()) for line in data]
tilt(grid, "N")
print(f"Part 1: {score(grid)}")

# Part 2. Find cycle
grid = [list(line.strip()) for line in data]
grids = {}
for i in range(1000000000):
    for d in ["N", "W", "S", "E"]:
        tilt(grid, d)
    t = tuple([tuple(x) for x in grid])
    if t in grids:
        break
    grids[t] = i

# Find where in the cycle 1B is
cycle_start = grids[t]
cycle_length = i - cycle_start
cycle_pos = (1000000000-cycle_start) % cycle_length
idx = cycle_start + cycle_pos - 1
for g,i in grids.items():
    if i == idx:
        print(f"Part 2: {score(g)}")
        break
