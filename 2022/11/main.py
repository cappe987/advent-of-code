import sys
sys.path.append('../')
from aoclib import *
import json
import math

# I did some work on the input beforehand to simplify parsing
# :%s/    If/ /g
# :%s/throw to monkey //g
# :%s/divisible by //g
# :%s/Starting items/items/g
# :%s/new = //g
# YAML -> JSON
# Added "" to single items that had not been interpreted as lists by converter

def parse():
    f = open("example.json")
    f = open("input.json")
    data = json.load(f)

    monkeys = []
    for m in data:
        data[m]["items"] = list(map(int, data[m]["items"].split(", ")))
        data[m]["Test"] = int(data[m]["Test"])
        data[m]["true"] = int(data[m]["true"])
        data[m]["false"] = int(data[m]["false"])
        op = eval(f'lambda old: {data[m]["Operation"]}')
        data[m]["Operation"] = op
        monkeys.append(data[m])
    return monkeys

def solve(iterations, part1):
    monkeys = parse()

    _lcm = 1
    for m in monkeys:
        _lcm = math.lcm(_lcm, m["Test"])
    inspects = [0 for _ in range(len(monkeys))]
    for r in range(iterations):
        for m in range(len(monkeys)):
            for old in monkeys[m]["items"]:
                inspects[m] += 1
                new = monkeys[m]["Operation"](old)
                worry = new // 3 if part1 else new % _lcm
                if worry % monkeys[m]["Test"] == 0:
                    monkeys[monkeys[m]["true"]]["items"].append(worry)
                else:
                    monkeys[monkeys[m]["false"]]["items"].append(worry)
            monkeys[m]["items"] = []
    return math.prod(sorted(inspects, reverse=True)[0:2])

print(f"Part 1: {solve(20, True)}")
print(f"Part 2: {solve(10000, False)}")
