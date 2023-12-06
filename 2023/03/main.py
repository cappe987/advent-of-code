import sys
sys.path.append('../')
from aoclib import *
from math import prod

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def in_range(i, j, grid):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

def get_neighbours(i, j, grid):
    return filter(lambda xy: in_range(xy[0], xy[1], grid), [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)])

def to_number(num, grid):
    return int("".join(map(lambda ij: grid[ij[0]][ij[1]], num)))

def part_1(grid):
    tot = 0
    for n in numbers:
        for ij in n:
            if any(map(lambda x: (not grid[x[0]][x[1]].isdigit()) and grid[x[0]][x[1]] != '.', get_neighbours(ij[0], ij[1], grid))):
                tot += to_number(n, grid)
                break
    return tot

def get_num_at(grid, i, j):
    coords = []
    if in_range(i, j-1, grid) and grid[i][j-1].isdigit():
        if in_range(i,j-2, grid) and grid[i][j-2].isdigit():
            coords.append((i,j-2))
        coords.append((i,j-1))
    coords.append((i,j))
    if in_range(i, j+1, grid) and grid[i][j+1].isdigit():
        coords.append((i,j+1))
        if in_range(i, j+2, grid) and grid[i][j+2].isdigit():
            coords.append((i,j+2))
    return to_number(coords, grid)

def neigh_digit(grid, i,j):
    digits = []
    if grid[i-1][j-1].isdigit():
        digits.append((i-1,j-1))
        if not grid[i-1][j].isdigit() and grid[i-1][j+1].isdigit():
            digits.append((i-1,j+1))
    elif grid[i-1][j].isdigit():
        digits.append((i-1,j))
    elif grid[i-1][j+1].isdigit():
        digits.append((i-1,j+1))

    if grid[i+1][j-1].isdigit():
        digits.append((i+1,j-1))
        if not grid[i+1][j].isdigit() and grid[i+1][j+1].isdigit():
            digits.append((i+1,j+1))
    elif grid[i+1][j].isdigit():
        digits.append((i+1,j))
    elif grid[i+1][j+1].isdigit():
        digits.append((i+1,j+1))

    if grid[i][j-1].isdigit():
        digits.append((i,j-1))
    if grid[i][j+1].isdigit():
        digits.append((i,j+1))

    if len(digits) == 2:
        return prod(map(lambda x: get_num_at(grid, x[0], x[1]), digits))

    return 0

def part_2(grid):
    tot = 0
    gears = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '*']
    for (i,j) in gears:
            # Optimized solution
            tot += neigh_digit(grid, i, j)

            # neigh_idx = list(filter(lambda x: grid[x[0]][x[1]].isdigit(), get_neighbours(i, j, grid)))
            # neighs = [n for n in numbers if any(map(lambda x: (x[0],x[1]) in neigh_idx, n))]
            # if len(neighs) == 2:
                # tot += to_number(neighs[0], grid) * to_number(neighs[1], grid)
    return tot

grid = list(map(lambda x: x.strip(), data))
numbers = []
for i in range(len(grid)):
    num = []
    for j in range(len(grid[0])):
        if grid[i][j].isdigit():
            num.append((i,j))
        elif len(num) > 0:
            numbers.append(num)
            num = []
    if len(num) > 0:
        numbers.append(num)

print(f"Part 1: {part_1(grid)}")
print(f"Part 2: {part_2(grid)}")

