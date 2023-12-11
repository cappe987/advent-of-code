import sys
sys.path.append('../')
from aoclib import *
from itertools import combinations

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def solve(grid, multiplier):
    galaxies = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#']
    empty_rows = [i for i in range(len(grid)) if all(map(lambda c: c == '.', grid[i]))]
    empty_cols = []
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i][j] != '.':
                break
        else:
            empty_cols.append(j)

    tot = 0
    for g1,g2 in combinations(galaxies, 2):
        empty_rows_between = 0
        for ri in empty_rows:
            if g1[0] < ri < g2[0] or g2[0] < ri < g1[0]:
                empty_rows_between += 1

        empty_cols_between = 0
        for ci in empty_cols:
            if g1[1] < ci < g2[1] or g2[1] < ci < g1[1]:
                empty_cols_between += 1

        tot += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]) + empty_rows_between*(multiplier-1) + empty_cols_between*(multiplier-1)
    return tot

grid = [list(line.strip()) for line in data]
print(f"Part 1: {solve(grid, 2)}")
print(f"Part 2: {solve(grid, 1000000)}")


