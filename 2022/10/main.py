import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()


def get_signal(cycle, reg):
    if (cycle % 40) == 20:
        return cycle * reg
    return 0

cycle = 1
signal = 0
reg = 1
for line in data:
    ops = line.strip().split()
    if ops[0] == "noop":
        cycle += 1
        signal += get_signal(cycle, reg)
    elif ops[0] == "addx":
        cycle += 1
        signal += get_signal(cycle, reg)
        cycle += 1
        reg += int(ops[1])
        signal += get_signal(cycle, reg)

print(f"Part 1: {signal}")

def write_sprite(screen, cycle, reg):
    n = (cycle % 40) 
    if n == reg-1 or n == reg or n == reg + 1:
        screen[cycle] = '#'

cycle = 0
reg = 1
screen = ['.' for _ in range(240)]
for line in data:
    ops = line.strip().split()
    if ops[0] == "noop":
        write_sprite(screen, cycle, reg)
        cycle += 1
    elif ops[0] == "addx":
        write_sprite(screen, cycle, reg)
        cycle += 1
        write_sprite(screen, cycle, reg)
        cycle += 1
        reg += int(ops[1])

print("Part 2:")
for row in iter_group(screen, 40):
    print("".join(row))

