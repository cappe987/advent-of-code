import sys
sys.path.append('../')
from aoclib import *
from heapq import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def move(pos, d):
    return pos[0]+d[0], pos[1]+d[1]

def part1(grid):
    start = (0,1)
    goal = (len(grid)-1,len(grid[0])-2)
    pq = []
    visited = set()

    dirs = {">": (0, 1), "v": (1, 0), "^": (-1, 0), "<": (0, -1)}
    opposite = {"<": ">", ">": "<", "v": "^", "^": "v"}

    pq = [(0, "v", start, {start})]
    grid[0][1] = '#'
    grid[goal[0]][goal[1]] = '#'

    high = 0

    while len(pq) > 0:
        ch, cd, cp, path = heappop(pq)

        visited.add((cp, cd))
        if grid[cp[0]][cp[1]] in dirs:
            np = move(cp, dirs[grid[cp[0]][cp[1]]])
            heappush(pq, (ch-1, cd, np, path | {np}))
            continue

        for d in dirs:
            np = move(cp, dirs[d])
            if np == goal:
                high = max(-(ch-1), high)
                res = (ch-1, d, np, path | {np})
                break
            if np in path:
                continue

            if not in_range_grid(grid, np[0], np[1]) or grid[np[0]][np[1]] == '#':
                continue

            if grid[np[0]][np[1]] in dirs and grid[np[0]][np[1]] != d:
                continue
            heappush(pq, (ch-1, d, np, path | {np}))

    return high

def part2(grid):
    start = (0,1)
    goal = (len(grid)-1,len(grid[0])-2)
    grid[0][1] = '#'

    nodes = dict()

    nodes[start] = []
    nodes[goal] = []

    # Find nodes
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                continue
            num = 0
            for (i2,j2) in grid_neighbours(grid, i, j):
                if grid[i2][j2] == '#':
                    num += 1
            if num < 2:
                nodes[(i,j)] = []

    # Calculate distance between nodes
    for node in nodes:
        q = [(node[0], node[1], 0)]
        visited = set([node])
        while q:
            (i, j, dist) = q.pop(0)

            if (i,j) in nodes and (i,j) not in visited:
                if ((i,j),dist) not in nodes[node]:
                    nodes[(i,j)].append((node, dist))
                    nodes[node].append(((i,j), dist))
                continue

            visited.add((i,j))

            for i2,j2 in grid_neighbours(grid, i, j):
                if grid[i2][j2] == '#' or (i2,j2) in visited:
                    continue
                q.append((i2,j2, dist+1))

    # Find longest path
    pq = [(0, start, set())]
    possible = []
    high = 0
    while pq:
        dist, node, path = heappop(pq)
        if node == goal:
            high = max(-dist, high)
            continue

        for (node2, dist2) in nodes[node]:
            if node2 in path:
                continue
            heappush(pq, (dist-dist2, node2, path | {node}))
            
    return high



grid = [list(x.strip()) for x in data]
print(f"Part 1: {part1(grid)}")

grid = [list(x.strip()) for x in data]
print(f"Part 2: {part2(grid)}")
