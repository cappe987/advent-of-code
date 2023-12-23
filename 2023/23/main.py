import sys
sys.path.append('../')
from aoclib import *
from heapq import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def move(pos, d):
    return pos[0]+d[0], pos[1]+d[1]

def solve(grid):
    start = (0,1)
    goal = (len(grid)-1,len(grid[0])-2)
    pq = []
    visited = set()

    dirs = {">": (0, 1), "v": (1, 0), "^": (-1, 0), "<": (0, -1)}
    opposite = {"<": ">", ">": "<", "v": "^", "^": "v"}

    # pq = [(0, "^", start, [start])]
    pq = [(0, "^", start, {start})]
    grid[0][1] = '#'
    grid[goal[0]][goal[1]] = '#'

    high = 0


    possibles = []

    while len(pq) > 0:
        ch, cd, cp, path = heappop(pq)
        # print(ch, cd, cp, path)

        # if (cp, cd) in visited:
            # continue
        # if cp in path:
            # continue

        visited.add((cp, cd))
        # if grid[cp[0]][cp[1]] in dirs:
            # np = move(cp, dirs[grid[cp[0]][cp[1]]])
            # # heappush(pq, (ch-1, cd, np, path+[np]))
            # heappush(pq, (ch-1, cd, np, path | {np}))
            # continue

        for d in dirs:
            np = move(cp, dirs[d])
            if np == goal:
                high = max(-(ch-1), high)
                print(f"Found length {-(ch-1)}. High = {high}")
                # res = (ch-1, d, np, path+[np])
                res = (ch-1, d, np, path | {np})
                possibles.append(res)
                break
            # if (np, d) in visited:
                # continue
            if np in path:
                continue

            if not in_range_grid(grid, np[0], np[1]) or grid[np[0]][np[1]] == '#':
                continue

            # if grid[np[0]][np[1]] in dirs and grid[np[0]][np[1]] != d:
                # continue

                # continue
            # nh = ch + grid[np[0]][np[1]]
            # if np == goal and (not part2 or d == cd[-1] and len(cd) >= 4):
                # return nh
            # heappush(pq, (ch-1, d, np, path+[np]))
            heappush(pq, (ch-1, d, np, path | {np}))

    # for res in possibles:
        # print(-res[0])

        # for i in range(len(grid)):
            # for j in range(len(grid[0])):
                # if (i,j) in res[3]:
                    # print('O', end='')
                # else:
                    # print(grid[i][j], end='')
            # print()
    # return res[0]
    return max(map(lambda x: -x[0], possibles))


grid = [list(x.strip()) for x in data]

print(f"Part 1: {solve(grid)}")


# 5858 too low
# print(f"Part 2: {res}")
