import sys
sys.path.append('../')
from aoclib import *

# data = open("example.txt").readlines()
# data = open("example2.txt").readlines()
data = open("input.txt").readlines()

strnums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
           "six": "6", "seven": "7", "eight": "8", "nine": "9"}
nums = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5",
        "6": "6", "7": "7", "8": "8", "9": "9"}

def get_number(line, nums):
    res = ""
    for i in range(len(line)):
        for s,n in nums.items():
            if line[i:].startswith(s):
                res += n
                break
    return int(res[0] + res[-1])

def solve(data, number_map):
    return sum(map(lambda line: get_number(line, number_map), data))

print(f"Part 1: {solve(data, nums)}")
print(f"Part 2: {solve(data, strnums | nums)}")
