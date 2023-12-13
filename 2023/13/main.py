import sys
sys.path.append('../')
from aoclib import *
from functools import reduce

data = open("example.txt").readlines()
data = open("input.txt").readlines()

data = iter_split(map(lambda y: list(y.strip()), data), lambda x: x == [])

def get_best(b1, b2, w, h):
    if b1 == None:
        return b2
    elif b2 == None:
        return b1
    b1mid = (b1[0]+b1[1])/2
    b2mid = (b2[0]+b2[1])/2
    w = len(grid)
    if abs(w/2 - b1mid) < abs(h/2 - b2mid):
        return b1
    else:
        return b2

def get_reflections(grid):
    refl = []
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:
            refl.append((i,i+1))

    perf_refl = []
    if len(refl) > 0:
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

def get_best_reflection(grid, xs):
    return reduce(lambda x,y: get_best(x, y, len(grid), len(grid)), xs)

def find_best_reflection(grid):
    mirror = get_reflections(grid)
    orig = get_best_reflection(grid, mirror) if mirror else None

    reflections = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            curr = grid[i][j]
            grid[i][j] = '#' if curr == '.' else '#'
            refl = get_reflections(grid)
            for r in refl:
                if r != orig:
                    reflections.append(r)
            grid[i][j] = curr

    return orig, get_best_reflection(grid, reflections) if reflections else None

def get_count(grid, best_row, best_col):
    if get_best(best_row, best_col, len(grid), len(grid[0])) == best_row:
        return (best_row[0]+1) * 100
    return best_col[0]+1
    
count = 0
count_2 = 0
for grid in data:
    h = len(grid)
    w = len(grid[0])

    best_row_p1, best_row_p2 = find_best_reflection(grid)
    grid = list(map(list, zip(*grid)))
    best_col_p1, best_col_p2 = find_best_reflection(grid)

    count += get_count(grid, best_row_p1, best_col_p1)
    count_2 += get_count(grid, best_row_p2, best_col_p2)

print(f"Part 1: {count}")
print(f"Part 2: {count_2}")
