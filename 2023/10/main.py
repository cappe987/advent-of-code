import sys
sys.path.append('../')
from aoclib import *

# grid = open("example.txt").readlines()
# grid = open("example2.txt").readlines()
# grid = open("example3.txt").readlines()
# grid = open("example4.txt").readlines()
# grid = open("example5.txt").readlines()
grid = open("input.txt").readlines()

dirs = {
    "|": [(-1,0), (1,0)],
    "-": [(0,-1), (0,1)],
    "L": [(-1,0), (0,1)],
    "J": [(-1,0), (0,-1)],
    "7": [(1,0), (0,-1)],
    "F": [(1,0), (0,1)],
    ".": [],
}

def get_neigh_pipes(grid, i, j):
    xs = dirs[grid[i][j]]
    return [(i+x[0],j+x[1]) for x in xs if in_range_grid(grid, i+x[0], j+x[1])]

grid = [row.strip() for row in grid]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i,j)
            break

visited = {start: 0}

start_neighs = list(grid_neighbours(grid, start[0], start[1]))
queue = [(x,1) for x in start_neighs if start in get_neigh_pipes(grid, x[0], x[1])]

while len(queue) > 0:
    pos, dist = queue.pop(0)

    if pos in visited:
        continue
    visited[pos] = dist

    for n in get_neigh_pipes(grid, pos[0], pos[1]):
        queue.append((n, dist+1))

print(f"Part 1: {max(visited.values())}")

def get_start_pipe(grid, s, n1, n2):
    above = False
    below = False
    left = False
    right = False
    if n1[0] == s[0] and n1[1] == s[1]+1 or n2[0] == s[0] and n2[1] == s[1]+1:
        right = True
    if n1[0] == s[0] and n1[1] == s[1]-1 or n2[0] == s[0] and n2[1] == s[1]-1:
        left = True
    if n1[0] == s[0]+1 and n1[1] == s[1] or n2[0] == s[0]+1 and n2[1] == s[1]:
        below = True
    if n1[0] == s[0]-1 and n1[1] == s[1] or n2[0] == s[0]-1 and n2[1] == s[1]:
        above = True

    if above and below:
        return '|'
    if left and right:
        return '-'
    if above and right:
        return 'L'
    if above and left:
        return 'J'
    if below and left:
        return '7'
    if below and right:
        return 'F'

# Replace S with actual pipe
n1,n2 = [x for x in start_neighs if start in get_neigh_pipes(grid, x[0], x[1])]
pipe = get_start_pipe(grid, start, n1, n2)
row = list(grid[start[0]])
row[start[1]] = pipe
grid[start[0]] = "".join(row)

# Crossing an odd numbers of lines indicates a location is inside the loop.
# Special handling for when going on edges like F---7 since that doesn't count
# as crossing a line. But crossing F---J counts.
count = 0
i,j = 0,0
crosses = 0
while i < len(grid):
    j = 0
    while j < len(grid[0]):
        if (i,j) in visited:
            if grid[i][j] in "FL":
                edgestart = grid[i][j]
                while grid[i][j] not in "7J":
                    j += 1
                if edgestart == "F" and grid[i][j] == "J" or edgestart == "L" and grid[i][j] == "7":
                    crosses += 1
            else:
                crosses += 1
        elif crosses % 2 == 1:
            count += 1

        j += 1
    i += 1

print(f"Part 2: {count}")
