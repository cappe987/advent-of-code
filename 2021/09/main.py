from queue import *


def neigh(x,y, height, width):
  return filter(lambda xy: xy[0] >= 0 and xy[1] >= 0 and xy[0] < height and xy[1] < width, [(x+1,y), (x-1,y), (x,y+1), (x,y-1)])

def is_lowest(field, x, y, height, width):
  for (x1,y1) in neigh(x,y, height, width):
    if field[x1][y1] <= field[x][y]:
      return False
  
  return True

def lowest_points(field):
  lowest = []
  for i in range(len(field)):
    for j in range(len(field[0])):
      if is_lowest(field, i, j, len(field), len(field[0])):
        lowest.append((i,j))
  
  return lowest

def solve_1(field):
  return sum(map(lambda xy: field[xy[0]][xy[1]]+1, lowest_points(field)))

def solve_2(field):
  basins = []
  for (x,y) in lowest_points(field):
    basin = set() # visited
    basin.add((x,y))
    q = Queue()
    q.put((x,y))
    while q.qsize() > 0:
      x1,y1 = q.get()
      for x2,y2 in neigh(x1,y1, len(field), len(field[0])):
        if field[x2][y2] < 9 and (x2,y2) not in basin:
          basin.add((x2,y2))
          q.put((x2,y2))
    
    basins.append(basin)

  ls = sorted(map(lambda b: len(b), basins), reverse=True)
  return ls[0] * ls[1] * ls[2]
      


def parse(filename):
  return [list(map(int, x.rstrip())) for x in open(filename)]


# data = parse("sample.txt")
data = parse("input.txt")
print(solve_1(data))
print(solve_2(data))