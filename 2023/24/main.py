import sys
sys.path.append('../')
from aoclib import *
import numpy as np

data = open("example.txt").readlines()
# data = open("example2.txt").readlines()
data = open("input.txt").readlines()


def parse_line(line):
    pos, vec = line.split('@')
    pos = list(map(int, pos.split(', ')))
    vec = list(map(int, vec.split(', ')))

    return pos,vec



def find_intersection(p1, v1, p2, v2):
    # print('==========')
    # print(p1, v1)
    # print(p2, v2)
    # x, err, rank = np.linalg.lstsq(np.array([v1, -v2]).T, p2-p1, rcond=None)[:3]
    # # print(x, err, rank)

    # if len(err) == 0 and rank == 2:
        # pint = v1 * x[0] + p1

        # x1,y1   = p1
        # x2,y2   = p2
        # dx1,dy1 = v1
        # dx2,dy2 = v2
            
        # dx = x2 - x1
        # dy = y2 - y1
        # det = dx2 * dy1 - dy2 * dx1
        # if det == 0: # Parallel
            # return None
        # u = (dy * dx2 - dx * dy2) / det
        # v = (dy * dx1 - dx * dy1) / det

        # if u > 0 and v > 0:
            # return pint

            # print('Intersects after')
        # else:
            # print('Intersects before')
    # else:
        # print('Never intersects')
    # return None


    x1,y1   = p1
    x2,y2   = p2
    dx1,dy1 = v1
    dx2,dy2 = v2
    
    dx = x2 - x1
    dy = y2 - y1
    det = dx2 * dy1 - dy2 * dx1
    if det == 0: # Parallel
        return None
    u = (dy * dx2 - dx * dy2) / det
    v = (dy * dx1 - dx * dy1) / det

    if u > 0 and v > 0:
        t = ((x2 - x1) * dy2 - (y2 - y1) * dx2) / (dx1 * dy2 - dy1 * dx2)
        x_int = x1 + dx1 * t
        y_int = y1 + dy1 * t
        return x_int, y_int
    return None


def part1(data, low, high):
    data = [(np.array(pos[:2]).T, np.array(vec[:2]).T) for pos,vec in data]
    # data = [(np.array(pos[:2], np.float64).T, np.array(vec[:2], np.float64).T) for pos,vec in data]
    # print(data)

    valids = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            p1,v1 = data[i]
            p2,v2 = data[j]
            pint = find_intersection(p1, v1, p2, v2)
            if pint is not None:
                if low <= pint[0] <= high and low <= pint[1] <= high:
                    valids += 1
                    # print('valid')

    return valids


data = [parse_line(line) for line in data]

# 24139 too high
# 23747 too high
# 5740 wrong
# res = part1(data, 7, 27)
res = part1(data, 200000000000000, 400000000000000)

# print(data)

print(f"Part 1: {res}")
# print(f"Part 2: {res}")




# print()
# v1 = np.array([4, 2, -1]).T
# c1 = np.array([6, 3, 2]).T
# v2 = np.array([5, -2, 3]).T
# c2 = np.array([-3, 3, 0]).T
# # in this case the solved x is [-1.  1.], error is 0, and rank is 2
# x, err, rank = np.linalg.lstsq(np.array([v1, -v2]).T, c2-c1, rcond=None)[:3]
# if rank == 2:
    # # intersection exists
    # print(v1 * x[0] + c1)
# else:
    # print("no intersection")

