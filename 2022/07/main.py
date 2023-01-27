import sys
sys.path.append('../')
from aoclib import *

import os

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def create_dirs(i, data):
    curr = []
    while i < len(data):
        if data[i].startswith("$ cd .."):
            i += 1
            break
        elif data[i].startswith("$ cd"):
            i += 1
            i, directory = create_dirs(i, data)
            curr.append(directory)
        elif data[i] == "$ ls":
            i += 1
            while i < len(data) and not data[i].startswith("$"):
                line = data[i].split()
                if line[0] != "dir":
                    curr.append(int(line[0]))
                i += 1
    return i, curr

def walk(curr, dirs):
    dirsize = 0
    for f in curr:
        if type(f) == list:
            size = walk(f, dirs)
            dirsize += size
        else:
            dirsize += f
    dirs.append(dirsize)
    return dirsize

data = list(map(lambda x: x.strip(), data[1:]))
_, filesystem = create_dirs(0, data)
dirs = []
walk(filesystem, dirs)
tot = sum(filter(lambda x: x < 100000, dirs))
print(f"Part 1: {tot}")

total_unused = 70000000 - max(dirs)
min_del = 30000000 - total_unused
to_del = min([size for size in dirs if size >= min_del])
print(f"Part 2: {to_del}")


