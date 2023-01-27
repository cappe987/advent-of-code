
import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

per_elf = iter_split(data, lambda x: x == '\n')
elftotals = [sum(map(parse_int, elf)) for elf in per_elf]
ranking = sorted(elftotals, reverse=True)

print(f"Part 1: {ranking[0]}")
print(f"Part 2: {sum(ranking[0:3])}")

