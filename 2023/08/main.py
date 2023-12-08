import sys
sys.path.append('../')
from aoclib import *
import math
from functools import reduce

data = open("example.txt").readlines()
data = open("example2.txt").readlines()
data = open("input.txt").readlines()

def part_1(steps, m):
    pos = 'AAA'
    count = 0
    i = 0

    while pos != 'ZZZ':
        pos = m[pos][steps[i]]
        i = (i+1) % len(steps)
        count += 1

    return count

def part_2(steps, m):
    starts = [x for x in m if x[2] == 'A']

    # Find the cycletimes. Turns out we don't even need to measure a cycle
    # after reaching an ending. The steps to reach an end state is the
    # cycletime.
    cycletimes = []
    for pos in starts:
        i = 0
        count = 0

        while True:
            pos = m[pos][steps[i]]
            i = (i + 1) % len(steps)
            count += 1
            if pos[2] == 'Z':
                break

        cycletimes.append(count)

    return math.lcm(*cycletimes)


steps = list(map(lambda x: 0 if x == 'L' else 1, data[0].strip()))

m = {}
for line in data[2:]:
    x = line.split()
    m[x[0]] = (x[2][1:4], x[3][:3])

print(f"Part 1: {part_1(steps, m)}")
print(f"Part 1: {part_2(steps, m)}")
