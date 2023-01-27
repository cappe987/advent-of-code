import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def has_full_overlap(outer, inner):
    return outer[0] <= inner[0] and outer[1] >= inner[1]

def has_overlap(a, b):
    return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]

def parse(data):
    for line in data:
        a,b = line.strip().split(',')
        a = list(map(int, a.split('-')))
        b = list(map(int, b.split('-')))
        yield (a,b)

parsed = parse(data)
full_overlaps = 0
total_overlaps = 0
for a,b in parsed:
    total_overlaps += has_overlap(a,b)
    full_overlaps += has_full_overlap(a,b) or has_full_overlap(b,a)

print(f"Part 1: {full_overlaps}")
print(f"Part 2: {total_overlaps}")
