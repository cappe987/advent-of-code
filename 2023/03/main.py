import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def in_range(i, j, data):
    return i >= 0 and i < len(data) and j >= 0 and j < len(data[0])

def get_neighbours(i, j, data):
    return filter(lambda xy: in_range(xy[0], xy[1], data), [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)])

def to_number(num, data):
    return int("".join(map(lambda ij: data[ij[0]][ij[1]], num)))

def part_1(data):
    tot = 0
    for n in numbers:
        for ij in n:
            if any(map(lambda x: (not data[x[0]][x[1]].isdigit()) and data[x[0]][x[1]] != '.', get_neighbours(ij[0], ij[1], data))):
                tot += to_number(n, data)
                break
    return tot

def part_2(data):
    tot = 0
    gears = [(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == '*']
    for (i,j) in gears:
            neigh_idx = list(get_neighbours(i, j, data))
            neighs = [n for n in numbers if any(map(lambda x: (x[0],x[1]) in neigh_idx, n))]
            if len(neighs) == 2:
                tot += to_number(neighs[0], data) * to_number(neighs[1], data)
    return tot

data = list(map(lambda x: x.strip(), data))
numbers = []
for i in range(len(data)):
    num = []
    for j in range(len(data[0])):
        if data[i][j].isdigit():
            num.append((i,j))
        elif len(num) > 0:
            numbers.append(num)
            num = []
    if len(num) > 0:
        numbers.append(num)

print(f"Part 1: {part_1(data)}")
print(f"Part 2: {part_2(data)}")

