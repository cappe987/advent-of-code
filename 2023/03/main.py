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

def part_1(grid, numbers):
    tot = 0
    for n in numbers:
        for ij in n:
            if any(map(lambda x: (not grid[x[0]][x[1]].isdigit()) and grid[x[0]][x[1]] != '.', get_neighbours(ij[0], ij[1], grid))):
                tot += to_number(n, grid)
                break
    return tot

def part_2(grid, numbers):
    tot = 0
    gears = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '*']
    for (i,j) in gears:
            neigh_idx = list(filter(lambda x: grid[x[0]][x[1]].isdigit(), get_neighbours(i, j, grid)))
            neighs = [n for n in numbers if any(map(lambda x: (x[0],x[1]) in neigh_idx, n))]
            if len(neighs) == 2:
                tot += to_number(neighs[0], grid) * to_number(neighs[1], grid)
    return tot

def part_2_opt(grid, numbers):
    gears = {}
    tot = 0
    for num in numbers:
        found = False
        for digit in num:
            for neigh in get_neighbours(digit[0],digit[1], grid):
                if grid[neigh[0]][neigh[1]] == '*':
                    found = True
                    if neigh in gears:
                        gears[neigh].append(num)
                    else:
                        gears[neigh] = [num]
                    break
            if found:
                break

    for gear in gears:
        if len(gears[gear]) == 2:
            tot += prod(map(lambda x: to_number(x, grid), gears[gear]))
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

print(f"Part 1: {part_1(grid, numbers)}")
print(f"Part 2: {part_2_opt(grid, numbers)}")

