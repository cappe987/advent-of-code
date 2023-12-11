import sys
sys.path.append('../')
from aoclib import *
from itertools import combinations

data = open("example.txt").readlines()
data = open("input.txt").readlines()

# def solve(grid, multiplier=1):
    # galaxies = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#']
    # empty_rows = [i for i in range(len(grid)) if all(map(lambda c: c == '.', grid[i]))]
    # empty_cols = [j for j in range(len(list(zip(*grid)))) if all(map(lambda c: c == '.', list(zip(*grid))[j]))]

    # tot = 0
    # for g1,g2 in combinations(galaxies, 2):
        # empty_rows_between = 0
        # for ri in empty_rows:
            # if g1[0] < ri < g2[0] or g2[0] < ri < g1[0]:
                # empty_rows_between += 1

        # empty_cols_between = 0
        # for ci in empty_cols:
            # if g1[1] < ci < g2[1] or g2[1] < ci < g1[1]:
                # empty_cols_between += 1

        # tot += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]) + empty_rows_between*(multiplier-1) + empty_cols_between*(multiplier-1)
    # return tot

# Solve both at once
def solve_puzzles(grid):
    galaxies = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#']
    empty_rows = [i for i in range(len(grid)) if all(map(lambda c: c == '.', grid[i]))]
    inverted = list(zip(*grid))
    empty_cols = [j for j in range(len(inverted)) if all(map(lambda c: c == '.', inverted[j]))]

    tot_p1 = 0
    tot_p2 = 0
    for g1,g2 in combinations(galaxies, 2):
        empty_rows_between = 0
        for ri in empty_rows:
            if g1[0] < ri < g2[0] or g2[0] < ri < g1[0]:
                empty_rows_between += 1

        empty_cols_between = 0
        for ci in empty_cols:
            if g1[1] < ci < g2[1] or g2[1] < ci < g1[1]:
                empty_cols_between += 1

        dist = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
        tot_p1 += dist + empty_rows_between*(2-1) + empty_cols_between*(2-1)
        tot_p2 += dist + empty_rows_between*(1000000-1) + empty_cols_between*(1000000-1)
    return tot_p1, tot_p2

grid = [list(line.strip()) for line in data]
p1, p2 = solve_puzzles(grid)
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")


