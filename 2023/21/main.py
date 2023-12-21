import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
# data = open("example2.txt").readlines()
data = open("input.txt").readlines()

grid = [line.strip() for line in data]

def neighbours(i, j):
    return [(i-1,j), (i,j-1), (i,j+1), (i+1,j)]

start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i,j)
            break


odd = set()
even = set([start])

steps = 64
# steps = 129
# steps = 26501365
# steps = 128

curr = set([start])
for step in range(1, steps+1):
    nxt = set()
    for (i,j) in curr:
        for (i2,j2) in neighbours(i, j):
            if not in_range_grid(grid, i, j):
                continue
            if grid[i2][j2] == '#':
                continue
            nxt.add((i2,j2))
            if step % 2 == 0:
                even.add((i2,j2))
            else:
                odd.add((i2,j2))

    curr = nxt
        
# for i in range(len(grid)):
    # for j in range(len(grid[0])):
        # if (i,j) in curr:
            # print('O', end='')
        # else:
            # print(grid[i][j], end='')
    # print()

print(len(curr))



# print(f"Part 1: {res}")
# print(f"Part 2: {res}")
