import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def neigh(p):
    return ((p[0]+1, p[1]), (p[0], p[1]+1), (p[0]-1, p[1]), (p[0], p[1]-1))

def in_range(grid, y, x):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])

def bfs(grid, start, end, startdist=0):
    answers = []
    visited = {}
    queue = []
    visited[start] = 0
    queue.append((start, startdist))

    while queue:
        yx, dist= queue.pop(0) 
        dist += 1

        for n in neigh(yx):
            if not in_range(grid, n[0], n[1]):
                continue
            if ord(grid[n[0]][n[1]]) > (ord(grid[yx[0]][yx[1]]) + 1):
                continue
            if n == end:
                answers.append(dist)
                break
            if n not in visited or dist < visited[n]:
                visited[n] = dist
                queue.append((n, dist))
    return answers

grid = list(map(lambda x:list(x.strip()), data))
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            start = (y,x)
        if grid[y][x] == "E":
            end = (y,x)

grid[start[0]][start[1]] = "a"
grid[end[0]][end[1]] = "z"
answers = bfs(grid, start, end)
print(f'Part 1: {min(answers)}')

# Gather all 'b' with an adjacent 'a'. Lowers search space by a lot
# since at least my input had many fewer 'b' than 'a'
all_b = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'b':
            for (ny,nx) in neigh((y,x)):
                if in_range(grid, ny, nx) and grid[ny][nx] == 'a':
                    all_b.append((y,x))
                    break

mini = 100000
for start in all_b:
    answers = bfs(grid, start, end, 1)
    mini = min(mini, *answers or [100000])

print(f'Part 2: {mini}')
