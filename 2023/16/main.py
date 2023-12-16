import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def solve(grid, start):
    visited = set()
    beams = [start]

    idx = 0
    while len(beams) > 0:
        beam = beams.pop(0)
        i,j = beam[0]
        im,jm = beam[1]

        if beam in visited:
            continue
        if not in_range_grid(grid, i, j):
            continue
        visited.add(beam)

        if grid[i][j] == '|' and beam[1][0] == 0:
            beams.append(((i+1,j),(1,0)))
            beams.append(((i-1,j),(-1,0)))
        elif grid[i][j] == '-' and beam[1][1] == 0:
            beams.append(((i,j+1),(0,1)))
            beams.append(((i,j-1),(0,-1)))
        elif grid[i][j] == '/':
            im,jm = -jm,-im
            beams.append(((i+im,j+jm),(im,jm)))
        elif grid[i][j] == '\\':
            im,jm = jm,im
            beams.append(((i+im,j+jm),(im,jm)))
        else:
            beams.append(((i+im,j+jm),(im,jm)))
    return len(set(map(lambda x: x[0], visited)))

grid = [x.strip() for x in data]
start = ((0,0), (0,1))
print(f"Part 1: {solve(grid, start)}")

high = 0
for i in range(len(grid)): # Top row
    high = max(high, solve(grid,((0,i), (1,0))))
for i in range(len(grid)): # Bottom row
    high = max(high, solve(grid,((0,len(grid)-1), (-1,0))))
for i in range(len(grid)): # Left row
    high = max(high, solve(grid,((i,0), (0,1))))
for i in range(len(grid)): # Right row
    high = max(high, solve(grid,((len(grid)-1,0), (0,-1))))

print(f"Part 2: {high}")
