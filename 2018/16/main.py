import sys
sys.path.append('../')
from aoclib import *
import json

# data = open("example.txt").readlines()
data = open("input.txt").readlines()


def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]
def addi(regs, a, b, c):
    regs[c] = regs[a] + b

def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]
def muli(regs, a, b, c):
    regs[c] = regs[a] * b

def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]
def bani(regs, a, b, c):
    regs[c] = regs[a] & b

def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]
def bori(regs, a, b, c):
    regs[c] = regs[a] | b

def setr(regs, a, b, c):
    regs[c] = regs[a]
def seti(regs, a, b, c):
    regs[c] = a

def gtir(regs, a, b, c):
    regs[c] = 1 if a > regs[b] else 0
def gtri(regs, a, b, c):
    regs[c] = 1 if regs[a] > b else 0
def gtrr(regs, a, b, c):
    regs[c] = 1 if regs[a] > regs[b] else 0

def eqir(regs, a, b, c):
    regs[c] = 1 if a == regs[b] else 0
def eqri(regs, a, b, c):
    regs[c] = 1 if regs[a] == b else 0
def eqrr(regs, a, b, c):
    regs[c] = 1 if regs[a] == regs[b] else 0


def parse(lines):
    before = json.loads("".join(list(dropwhile(lambda x:x != ' ', lines[0].strip()))[1:]))
    ops = list(map(int, lines[1].strip().split()))
    after = json.loads("".join(list(dropwhile(lambda x:x != ' ', lines[2].strip()))[1:]))
    return before, ops, after

opstr   = ["addr", "addi", 'mulr', "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

operations = {name:op for name,op in zip(opstr, opcodes)}

data = iter_split(data, lambda x: x == "\n")


opers = list(takewhile(lambda x: x != [], data))
rest = list(dropwhile(lambda x: x != [], data))[2:]

possibles = {opname:set() for opname in opstr}
answer = 0
for operation in opers:
    count = 0
    before, ops, after = parse(operation)
    for opname, op in zip(opstr, opcodes):
        regs = before[:]
        op(regs, ops[1], ops[2], ops[3])
        if after == regs:
            possibles[opname].add(ops[0])
            count += 1

    if count >= 3:
        answer += 1

print(f"Part 1: {answer}")

opnums = {}

while len(possibles) > 0:
    found = False
    for name in possibles:
        if len(possibles[name]) == 1:
            num = list(possibles[name])[0]
            opnums[name] = num
            del possibles[name]
            found = True
            break

    if found:
        for name in possibles:
            if num in possibles[name]:
                possibles[name].remove(num)


numops = {num:name for name,num in opnums.items()}

regs = [0,0,0,0]
for action in rest[0]:
    op,a,b,c = list(map(int, action.strip().split()))
    operations[numops[op]](regs, a, b, c)

print(f"Part 2: {regs[0]}")


