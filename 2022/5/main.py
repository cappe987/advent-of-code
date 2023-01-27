import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def parse(data):
    stacks = list(takewhile(lambda x: x!='\n', data))
    steps = list(dropwhile(lambda x: x!='\n', data))[1:]
    cargo = [[] for _ in range(10)]
    for line in stacks:
        for i,crate in enumerate(iter_group(line, 4)):
            if crate[1] != ' ' and not crate[1].isdigit():
                cargo[i] = [crate[1]] + cargo[i]
    return cargo, steps

def solve(cargo, steps, part1):
    for line in steps:
        instr = line.split()
        amount, fro, to = int(instr[1]), int(instr[3]), int(instr[5])
        if part1:
            cargo[to-1].extend(cargo[fro-1][-1:-1-amount:-1])
        else:
            cargo[to-1].extend(reversed(cargo[fro-1][-1:-1-amount:-1]))
        cargo[fro-1] = cargo[fro-1][:len(cargo[fro-1])-amount]
    return "".join([x[-1] for x in cargo if len(x)>0])

print("Part 1:", solve(*parse(data), True))
print("Part 2:", solve(*parse(data), False))
