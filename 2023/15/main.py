import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()[0]
data = open("input.txt").readlines()[0]

def hash(s):
    curr = 0
    for c in s:
        curr = ((curr + ord(c)) * 17) % 256
    return curr

data = data.strip().split(',')

print(f"Part 1: {sum(map(hash, data))}")

boxes = [{} for _ in range(256)]

for instr in data:
    if instr[-1].isdigit():
        label,num = instr.split('=')
        boxes[hash(label)][label] = int(num)
    else:
        label = instr[:-1]
        box = boxes[hash(label)]
        if label in box:
            del box[label]

total = 0
for i,box in enumerate(boxes, 1):
    for j,lens in enumerate(box, 1):
        total += i * j * box[lens]
print(f"Part 2: {total}")
