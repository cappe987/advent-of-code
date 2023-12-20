import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
# data = open("example2.txt").readlines()
data = open("input.txt").readlines()



def parse_rule(line):
    name, rules = line.split('{')
    rules = rules[:-2]

    rules = rules.split(',')
    end = rules[-1]
    rules = rules[:-1]
    ruledata = []
    for r in rules:
        cond, dest = r.split(':')
        if '<' in cond:
            var, num = cond.split('<')
            num = int(num)
            ruledata.append((var, '<', num, dest))
        elif '>' in cond:
            var, num = cond.split('>')
            num = int(num)
            ruledata.append((var, '>', num, dest))

    # print(name, ruledata, end)
    return (name, ruledata, end)

def parse_item(line):
    line = line[1:-2].split(',')
    d = {}
    for var in line:
        name, val = var.split('=')
        val = int(val)
        d[name] = val
    return d


def solve_item(rules, rulename, item):
    if rulename == "R":
        return False
    if rulename == "A":
        return True

    ruledata, end = rules[rulename]
    # print(ruledata)
    for (var, cmp, num, dest) in ruledata:
        if cmp == '<':
            if item[var] < num:
                return solve_item(rules, dest, item)
        if cmp == '>':
            if item[var] > num:
                return solve_item(rules, dest, item)

    return solve_item(rules, end, item)
    


rules, items = iter_split(data, lambda x: x == "\n")

ruledict = {}
for r in rules:
    name, _r, end = parse_rule(r)
    ruledict[name] = (_r, end)
# print(ruledict)

# parsed_items = []
tot = 0
for i in items:
    item = parse_item(i)
    if solve_item(ruledict, 'in', item):
        tot += sum([item[x] for x in ['x', 'm', 'a', 's']])
    # parsed_items.append(item)

print(f"Part 1: {tot}")

def invert_rule(rule):
    var, cmp, num, dest = rule
    if cmp == '>':
        cmp = '<'
        num = num+1
    elif cmp == '<':
        cmp = '>'
        num = num-1
    return (var,cmp,num)

def invert_rules(rules):
    new = []
    for rule in rules:
        new.append(invert_rule(rule))
    return new

def part2(rules, rulename, conds):
    if rulename == "R":
        return []
    if rulename == "A":
        return conds
    tot = 0
    ruledata, end = rules[rulename]
    new_conds = []
    prev = []
    for (var, cmp, num, dest) in ruledata:
        c = part2(rules, dest, conds + prev + [(var,cmp,num)])
        if len(c) != 0:
            new_conds.append(c)
        prev.append(invert_rule((var,cmp,num,dest)))

    # inverted = invert_rules(ruledata)
    c = part2(rules, end, conds + prev)

    # new_conds.append()
    if len(c) != 0:
        # print('C', rulename, c)
        # print(rulename, c, '--------', inverted)
        # inverted.extend(c)
        # inverted.extend(c)
        new_conds.append(c)

    return new_conds
    
def flatten(ls, res):
    if type(ls) != list:
        return
    # print(ls)
    added = False
    for x in ls:
        if not added and type(x) != list:
            res.append(ls)
            added = True
        flatten(x, res)
 
res = part2(ruledict, 'in', [])
# print(res)
# print(res[1])

# print()

# All possible paths to get accepted
flattened = []
flatten(res, flattened)
# for x in flattened:
    # print(x)


# Example:
# 16740907986800

# print('=============')

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
    # print(rn)
    tmp = 1
    for x in ['x', 'm', 'a', 's']:
        tmp *=  rn[x][1] - rn[x][0] + 1
    tot += tmp

print(f"Part 2: {tot}")
