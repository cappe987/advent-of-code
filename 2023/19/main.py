import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def parse_workflow(line):
    name, ruledata = line.split('{')
    ruledata = ruledata[:-2]
    ruledata = ruledata.split(',')
    end = ruledata[-1]
    ruledata = ruledata[:-1]
    rules = []
    for r in ruledata:
        cond, dest = r.split(':')
        if '<' in cond:
            var, num = cond.split('<')
            num = int(num)
            rules.append((var, '<', num, dest))
        elif '>' in cond:
            var, num = cond.split('>')
            num = int(num)
            rules.append((var, '>', num, dest))

    return (name, rules, end)

def parse_item(line):
    line = line[1:-2].split(',')
    d = {}
    for var in line:
        name, val = var.split('=')
        val = int(val)
        d[name] = val
    return d

# Part 1
def solve_item(workflows, name, item):
    if name == "R":
        return False
    if name == "A":
        return True

    rules, end = workflows[name]
    for (var, cmp, num, dest) in rules:
        if cmp == '<':
            if item[var] < num:
                return solve_item(workflows, dest, item)
        if cmp == '>':
            if item[var] > num:
                return solve_item(workflows, dest, item)

    return solve_item(workflows, end, item)

# Part 2
def invert_rule(rule):
    var, cmp, num, dest = rule
    if cmp == '>':
        cmp = '<'
        num = num+1
    elif cmp == '<':
        cmp = '>'
        num = num-1
    return (var,cmp,num)

def find_paths(workflows, name, conds):
    if name == "R":
        return []
    if name == "A":
        return conds
    tot = 0
    rules, end = workflows[name]
    new_conds = []
    inverted = []
    for (var, cmp, num, dest) in rules:
        c = find_paths(workflows, dest, conds + inverted + [(var,cmp,num)])
        if c:
            new_conds.append(c)
        inverted.append(invert_rule((var,cmp,num,dest)))

    c = find_paths(workflows, end, conds + inverted)
    if c:
        new_conds.append(c)

    return new_conds
    
def flatten(ls, res):
    if type(ls) != list:
        return
    added = False
    for x in ls:
        if not added and type(x) != list:
            res.append(ls)
            added = True
        flatten(x, res)
 
    
rules, items = iter_split(data, lambda x: x == "\n")

ruledict = {}
for r in rules:
    name, _r, end = parse_workflow(r)
    ruledict[name] = (_r, end)

tot = 0
for i in items:
    item = parse_item(i)
    if solve_item(ruledict, 'in', item):
        tot += sum([item[x] for x in ['x', 'm', 'a', 's']])

print(f"Part 1: {tot}")

# All possible paths to get accepted
res = find_paths(ruledict, 'in', [])
flattened = []
flatten(res, flattened)

ranges = []
for x in flattened:
    valid_ranges = {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000)}
    for (var, cmp, val) in x:
        if cmp == '<':
            curr = valid_ranges[var]
            if curr[1] > val:
                valid_ranges[var] = (curr[0], val-1)
        if cmp == '>':
            curr = valid_ranges[var]
            if curr[0] < val:
                valid_ranges[var] = (val+1, curr[1])

    ranges.append(valid_ranges)

tot = 0
for rn in ranges:
    tmp = 1
    for x in ['x', 'm', 'a', 's']:
        tmp *=  rn[x][1] - rn[x][0] + 1
    tot += tmp

print(f"Part 2: {tot}")
