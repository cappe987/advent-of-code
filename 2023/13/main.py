import sys
sys.path.append('../')
from aoclib import *
from functools import reduce

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def get_reflections(grid):
    refl = [(i,i+1) for i in range(len(grid)-1) if grid[i] == grid[i+1]]

    perf_refl = []
    for i,j in refl:
        i2,j2 = i,j
        while i2 >= 0 and j2 < len(grid):
            if grid[i2] != grid[j2]:
                break
            i2 -= 1
            j2 += 1
        else:
            perf_refl.append((i,j))
    return perf_refl

def find_best_reflection(grid):
    mirror = get_reflections(grid)
    orig = mirror[0] if mirror else None

    reflections = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            curr = grid[i][j]
            grid[i][j] = '#' if curr == '.' else '#'
            for r in get_reflections(grid):
                if r != orig:
                    reflections.append(r)
            grid[i][j] = curr

    return orig, reflections[0] if reflections else None

def get_count(grid, row, col):
    if row:
        return (row[0]+1) * 100
    return col[0]+1
    
data = iter_split(map(lambda y: list(y.strip()), data), lambda x: x == [])
count_1 = 0
count_2 = 0
for grid in data:
    row_p1, row_p2 = find_best_reflection(grid)
    grid = list(map(list, zip(*grid)))
    col_p1, col_p2 = find_best_reflection(grid)

    count_1 += get_count(grid, row_p1, col_p1)
    count_2 += get_count(grid, row_p2, col_p2)

print(f"Part 1: {count_1}")
print(f"Part 2: {count_2}")
