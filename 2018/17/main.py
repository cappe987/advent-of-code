import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
# data = open("input.txt").readlines()

def parse_range(s):
    if "." in s:
        l, _, h = s.split(".")
        return (int(l), int(h))
    return int(s)


def parse(line):
    l1, l2 = line.split(',')
    l2 = l2.strip()
    if l1[0] == "x":
        xl = parse_range(l1[2:])
        yl = parse_range(l2[2:])
    else:
        xl = parse_range(l2[2:])
        yl = parse_range(l1[2:])
    return xl, yl

min_y = 0
min_x = float("inf")
max_x = float("-inf")


parsed_data = [parse(line) for line in data]
clay = set()

for x,y in parsed_data:
    if type(y) is tuple:
        for y in range(y[0], y[1]+1):
            clay.add((x,y))
    else:
        for x in range(x[0], x[1]+1):
            clay.add((x,y))

print(clay)


for x,y in parsed_data:
    if type(y) is tuple:
        min_y = max(y[1], min_y)
    else:
        min_y = max(y, min_y)
    if type(x) is tuple:
        min_x = min(x[1], min_x)
        max_X = max(x[1], max_x)
    else:
        min_x = min(x, min_x)
        max_x = max(x, max_x)

print(min_y)
print(min_x, max_x)


# still_water = set()
# sandwater = set()

# queue = []

# while queue:
    # xy = queue.pop(0)


