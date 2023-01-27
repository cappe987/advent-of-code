import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def visible(forest, inverted, height, width, y, x):
    curr = forest[y][x]
    vis = lambda curr, arr: max(arr or [-1]) < curr
    return (  vis(curr, forest[y][:x])
           or vis(curr, forest[y][x+1:width])
           or vis(curr, inverted[x][:y])
           or vis(curr, inverted[x][y+1:height]))

def view(curr, arr):
    ls = list(arr)
    if len(ls) == 0:
        return 0
    trees = len(list(takewhile(lambda x: x < curr, ls)))
    return trees if trees == len(ls) else trees+1

def scenic_view(forest, inverted, height, width, y, x):
    curr = forest[y][x]
    return ( view(curr, reversed(forest[y][:x]))
           * view(curr, forest[y][x+1:width])
           * view(curr, reversed(inverted[x][:y]))
           * view(curr, inverted[x][y+1:height])
           )

height = len(data)
width = len(data[0].strip())
forest = [[int(tree) for tree in row.strip()] for row in data]
inverted = list(zip(*forest))

tot = 0
for y in range(height):
    for x in range(width):
        tot += visible(forest, inverted, height, width, y, x)
print(f"Part 1: {tot}")

high = 0
for y in range(height):
    for x in range(width):
        high = max(high, scenic_view(forest, inverted, height, width, y, x))
print(f"Part 2: {high}")


# Alternative solution to part 1, but doesn't transfer to part 2
# print("-----------")
# def fill(visTrees, forest, start, end, step, invert):
    # for y in range(start, end, step):
        # high = -1
        # for x in range(start, end, step):
            # _y,_x = (x,y) if invert else (y,x)
            # visTrees[_y][_x] = visTrees[_y][_x] or forest[_y][_x] > high 
            # high = max(high, forest[_y][_x])

# length = len(data)
# forest = [[int(tree) for tree in row.strip()] for row in data]
# visTrees = [[False for _ in range(length)] for _ in range(length)]
# argsList = [(0,length,1,False), (0,length,1,True), (length-1,-1,-1,False), (length-1,-1,-1,True)]
# for args in argsList:
    # fill(visTrees, forest, *args)
# total = sum(map(sum, visTrees))
# print(f"Part 1: {total}")

