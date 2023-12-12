import sys
sys.path.append('../')
from aoclib import *
from functools import lru_cache

data = open("example.txt").readlines()
data = open("input.txt").readlines()

@lru_cache
def recurse(m, nums, group_count):
    if not m:
        return len(nums) == 0 and group_count == 0 or len(nums) == 1 and nums[0] == group_count

    count = 0
    possible = ['#', '.'] if m[0] == '?' else m[0]
    for p in possible:
        if p == '#':
            if nums and nums[0] > group_count:
                count += recurse(m[1:], nums, group_count+1)
        else:
            if group_count:
                if nums and nums[0] == group_count:
                    count += recurse(m[1:], nums[1:], 0)
            else:
                count += recurse(m[1:], nums, 0)

    return count

def solve(multiplier):
    def _solve(line):
        m, nums = line.split()
        nums = tuple(map(int, nums.split(',')))
        m = "?".join([m for _ in range(multiplier)])
        return recurse(m, nums*multiplier, 0)
    return _solve

print(f"Part 1: {sum(map(solve(1), data))}")
print(f"Part 2: {sum(map(solve(5), data))}")
