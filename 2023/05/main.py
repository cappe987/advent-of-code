import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

seeds = list(map(int, data[0][7:].split()))

rulegroups = iter_split(data[2:], lambda x: x == "\n")
rulegroups = list(map(lambda x: list(map(
                        lambda y: list(map(int, y.split())),
                        x[1:])),
                      rulegroups))

def part_1(seeds, rulegroups):
    for group in rulegroups:
        for i in range(len(seeds)):
            for rule in group:
                if seeds[i] >= rule[1] and seeds[i] < (rule[1] + rule[2]):
                    seeds[i] += (rule[0] - rule[1])
                    break
    return min(seeds)

def part_2(seeds, rulegroups):
    # Use (start, end) instead of (start, length)
    seeds = list(map(lambda x: [x[0],x[0]+x[1]-1], iter_group(seeds,2)))

    for group in rulegroups:
        i = 0
        while i < len(seeds):
            for rule in group:
                r1, r2 = rule[1], rule[1]+rule[2]
                s1, s2 = seeds[i][0], seeds[i][1]
                offset = rule[0] - rule[1]

                if s2 < r1 or s1 > r2: # Non-overlapping range
                    continue
                elif r1 <= s1 < r2 and s2 > r2: # Partial overlap
                    included = [s1+offset, r2-1+offset]
                    excluded = [r2, s2]
                    seeds[i] = included
                    seeds.append(excluded)
                    break
                elif r1 <= s2 < r2 and s1 < r1: # Partial overlap
                    included = [r1+offset, s2+offset]
                    excluded = [s1, r1-1]
                    seeds[i] = included
                    seeds.append(excluded)
                    break
                elif r1 <= s1 and s2 < r2: # Full overlap (like part 1)
                    seeds[i][0] += offset
                    seeds[i][1] += offset
                    break
            i += 1

    return min(map(lambda x: x[0], seeds))

print(f"Part 1: {part_1(seeds[:], rulegroups)}")
print(f"Part 2: {part_2(seeds, rulegroups)}")

