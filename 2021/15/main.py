from collections import defaultdict
from queue import Queue
from heapq import *

def print_grid(grid):
  for row in grid:
    print(row)

def parse(filename):
  return [list(map(int, row.rstrip())) for row in open(filename)]


def in_range(xy, size):
  return xy[0] >= 0 and xy[1] >= 0 and xy[0] < size and xy[1] < size

def neigh(x,y, size):
  return list(filter(lambda xy: in_range(xy, size), [(x+1, y), (x-1, y), (x ,y+1), (x, y-1)]))

def heur(xy, size):
  return (size - 1 - xy[0]) + (size - 1 - xy[1])

def incr(r, i):
  return r+i if r+i < 10 else (r+i) % 10 + 1
def extend_grid(grid):
  size = len(grid)
  for i in range(1, 5):
    for j in range(size):
      grid.append(list(map(lambda r: incr(r,i), grid[j])))

  for j in range(len(grid)):
    row = grid[j]
    orig = row[:]
    for i in range(1, 5):
      row.extend(list(map(lambda r: incr(r,i), orig)))




def bestfs(grid):
  visited = set()
  size = len(grid)
  visited.add((0,0))
  pq = []
  heappush(pq, (heur((0,0), len(grid)), 0, (0,0), []))
  currLow = defaultdict(lambda: 999999999)
  currLow[(0,0)] = 0
  while len(pq) > 0:
    pos = heappop(pq)
    if pos[2] == (size-1, size-1):
      return pos[1]
    for xy in neigh(pos[2][0], pos[2][1], size):
      risk = grid[xy[0]][xy[1]] + pos[1]
      if xy not in visited:
        visited.add(xy)
        hr = risk
        heappush(pq, (hr, risk, xy, pos[3] + [xy]))
        currLow[xy] = risk
      elif currLow[xy] > risk:
        i = list(map(lambda x: x[2], pq)).index(xy)
        if pq[i][0] > risk:
          pq[i] = pq[-1]
          heappop(pq)
          heapify(pq)
          heappush(pq, (risk, risk, xy))







# filename = "sample.txt"
filename = "input.txt"

grid = parse(filename)
print(bestfs(grid))
extend_grid(grid)
print(bestfs(grid))