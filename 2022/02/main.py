import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def get_lose(a):
    if a == "R":
        return "S"
    if a == "P":
        return "R"
    if a == "S":
        return "P"

def get_win(a):
    if a == "R":
        return "P"
    if a == "P":
        return "S"
    if a == "S":
        return "R"

def to_symbols(a,b, part1):
    if a == "A":
        a_s = "R"
    if a == "B":
        a_s = "P"
    if a == "C":
        a_s = "S"

    if part1:
        if b == "X":
            b_s = "R"
        if b == "Y":
            b_s = "P"
        if b == "Z":
            b_s = "S"
    else:
        if b == "X":
            b_s = get_lose(a_s)
        if b == "Y":
            b_s = a_s
        if b == "Z":
            b_s = get_win(a_s)

    return a_s, b_s


def symbol_to_points(s):
    if s == "R":
        return 1
    if s == "P":
        return 2
    if s == "S":
        return 3

def compete(a, b):
    if a == "R":
        if b == "R":
            return (3+symbol_to_points(a), 3+symbol_to_points(b))
        if b == "P":
            return (0+symbol_to_points(a), 6+symbol_to_points(b))
        if b == "S":
            return (6+symbol_to_points(a), 0+symbol_to_points(b))
    if a == "P":
        if b == "R":
            return (6+symbol_to_points(a), 0+symbol_to_points(b))
        if b == "P":
            return (3+symbol_to_points(a), 3+symbol_to_points(b))
        if b == "S":
            return (0+symbol_to_points(a), 6+symbol_to_points(b))
    if a == "S":
        if b == "R":
            return (0+symbol_to_points(a), 6+symbol_to_points(b))
        if b == "P":
            return (6+symbol_to_points(a), 0+symbol_to_points(b))
        if b == "S":
            return (3+symbol_to_points(a), 3+symbol_to_points(b))


total_you = 0
total_other = 0
for line in data:
    a,b = line.split()
    a,b = to_symbols(a,b, True)
    other, you = compete(a,b)
    total_other += other
    total_you += you
print("Part 1:", total_you)

total_you = 0
total_other = 0
for line in data:
    a,b = line.split()
    a,b = to_symbols(a,b, False)
    other, you = compete(a,b)
    total_other += other
    total_you += you
print("Part 2:", total_you)
