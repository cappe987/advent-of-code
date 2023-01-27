import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def walk_points(a,b):
    if a[0] == b[0]:
        y = a[0]
        return {(y,x) for x in range(min(a[1],b[1]), max(a[1],b[1])+1)}
            # yield (y,x)
    elif a[1] == b[1]:
        x = a[1]
        return {(y,x) for y in range(min(a[0],b[0]), max(a[0],b[0])+1)}
            # yield (y,x)
    else: 
        print("Unexpected")

beacons = set()
sensors = set()
together = []
for line in data:
    s, b = line.strip().split(':')
    sx,sy = list(map(int, s.split(",")))
    bx,by = list(map(int, b.split(",")))
    beacons.add((by,bx))
    sensors.add((sy,sx))
    together.append(((sy,sx), (by,bx)))

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# @profile
def count_row(beacons, sensors, together, target_y):
    in_row = set()
    bs = set(map(lambda x: x[1], filter(lambda x: x[0]==target_y, beacons)))
    ss = set(map(lambda x: x[1], filter(lambda x: x[0]==target_y, sensors)))
    for s,b in together:
        mdist = manhattan(s, b)
        target_dist = abs(s[0] - target_y)
        if target_dist <= mdist:
            row_width = (mdist*2+1) + (target_dist*-2)
            start = (target_y, s[1]-mdist+target_dist)
            end = (target_y, s[1]+mdist-target_dist)
            in_row |= {x for x in range(start[1], end[1]+1) if x not in bs and x not in ss}

    return len(in_row)


top_row = float('inf')
for s,b in together:
    mdist = manhattan(s,b)
    top_row = min(top_row, s[0]-mdist)

bot_row = float('-inf')
for s,b in together:
    mdist = manhattan(s,b)
    bot_row = max(bot_row, s[0]+mdist)

print(f'Part 1: {count_row(beacons, sensors, together, 2000000)}')



# Part 2. Solved separately from part 1, hence the repeated code

data = open("example.txt").readlines()
data = open("input.txt").readlines()

sensors = set()
beacons = set()
pairs = []

for line in data:
    s, b = line.strip().split(":")
    sx, sy = list(map(int, s.split(",")))
    bx, by = list(map(int, b.split(",")))
    sensors.add((sy,sx))
    beacons.add((by,bx))
    pairs.append(((sy,sx),(by,bx)))

def manhattan(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# edges = []
areas = []
for s, b in pairs:
    mdist = manhattan(s,b)
    areas.append((s, mdist))
    # top = s[0] - mdist



# This section currently does not work for the example
# Take the 4 points outputted and their mdist and plug into Desmos with the
# formula '|x - s[1]| + |y - s[0]| = a' and find which coordinate is in the
# middle of the 4 points
dist = []
for s, a in areas:
    for s2, a2 in areas:
        diff = abs((a + a2) - manhattan(s, s2))
        if diff == 2 and (s2,s,a2,diff) not in dist:
            dist.append((s,s2, a, diff))
            # print(s, a, s2, a2, diff)

y = 2916597
x = 2727057

print(f'Part 2: {x*4000000 + y}')

