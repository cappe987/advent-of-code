import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def char_to_value(c):
    if c.isupper(): return ord(c) - 38
    else: return ord(c) - 96

total = 0
for line in map(lambda x: x.strip(), data):
    a = line[:len(line)//2]
    b = line[len(line)//2:]
    total += char_to_value(list(set(a) & set(b))[0])
print(f"Part 1: {total}")
 
total = 0
for a,b,c in iter_group(map(lambda x: x.strip(), data), 3):
    total += char_to_value(list(set(a) & set(b) & set(c))[0])
print(f"Part 2: {total}")
