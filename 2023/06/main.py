import sys
sys.path.append('../')
from aoclib import *
from math import prod, sqrt, floor, ceil

data = open("example.txt").readlines()
data = open("input.txt").readlines()

# def ways_to_win(time, distance):
    # count = 0
    # for i in range(time):
        # if i * (time-i) > distance:
            # count += 1
    # return count

# Don't loop more than necessary
# def ways_to_win(time, distance):
    # count = 0
    # for i in range(time):
        # if i * (time-i) > distance:
            # lower = i
            # break
    # for i in range(time-1, -1, -1):
        # if i * (time-i) > distance:
            # upper = i
            # break
    # return upper-lower+1

# Quadratic formula
def ways_to_win(time, distance):
    mini = (time - sqrt(time**2 - 4*distance))/2
    maxi = (time + sqrt(time**2 - 4*distance))/2

    return ceil(maxi-1) - floor(mini+1) + 1

time_distance = zip(map(int, data[0][11:].split()), map(int, data[1][11:].split()))
res = prod(map(lambda x: ways_to_win(x[0], x[1]), time_distance))
print(f"Part 1: {res}")

time, distance = int("".join(data[0][11:].split())), int("".join(data[1][11:].split()))
res = ways_to_win(time, distance)
print(f"Part 2: {res}")
