
def parse(filename):
  return [list(map(int, x.rstrip())) for x in open(filename).readlines()]

def neigh(x,y, size):
  xs = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]

  return list(filter(lambda xy: xy[0] >= 0 and xy[1] >= 0 and xy[0] < size and xy[1] < size, xs))

def flash_neigh(grid, flashed, x, y):
  flashes = 0
  q = neigh(x,y, len(grid))
  visited = set()
  visited.add((x,y))
  while len(q) > 0:
    (x1,y1) = q.pop()
    visited.add((x1,y1))
    if (x1,y1) not in flashed:
      grid[x1][y1] += 1
      if grid[x1][y1] == 10:
        flashes += 1
        grid[x1][y1] = 0
        flashed.add((x1,y1))
        q.extend(neigh(x1, y1, len(grid)))

  return flashes

def print_grid(grid):
  for i in range(len(grid)):
    print(grid[i])

def run(grid, part1):
  flashes = 0
  i = 0
  cond = lambda a: a < 100 if part1 else lambda a: True
  while cond(i):
    i += 1
    flashed = set()
    new_flashes = 0
    for x in range(len(grid)):
      for y in range(len(grid[0])):
        if (x,y) not in flashed:
          grid[x][y] += 1
          if grid[x][y] == 10:
            new_flashes += 1
            grid[x][y] = 0
            flashed.add((x,y))
            new_flashes += flash_neigh(grid, flashed, x, y)
    if not part1 and new_flashes == (len(grid) * len(grid)):
      return i
    flashes += new_flashes

  return flashes
    
# filename = "sample.txt"
filename = "input.txt"

print(run(parse(filename), True))
print(run(parse(filename), False))