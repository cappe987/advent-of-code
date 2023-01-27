import sys
sys.path.append('../')
from aoclib import *

# data = open("example.txt").read().strip()
data = open("input.txt").read().strip()

def solve(data, length):
    for i in range(len(data)):
        if len(set(data[i:i+length])) == length:
            return i+length

print(f"Part 1: {solve(data, 4)}")
print(f"Part 2: {solve(data, 14)}")
