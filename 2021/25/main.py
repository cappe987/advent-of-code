
def parse(filename):
  return [list(x.rstrip()) for x in open(filename)]

def move(grid):
  height = len(grid)
  width = len(grid[0])
  
  # East-facing
  move_east = []
  for y in range(height):
    for x in range(width):
      if grid[y][x] == '>' and grid[y][(x+1) % width] == '.':
        move_east.append((y,x))
  
  for (y,x) in move_east:
    grid[y][x] = '.'
    grid[y][(x+1) % width] = '>'
  
  # South-facing
  move_south = []
  for y in range(height):
    for x in range(width):
      if grid[y][x] == 'v' and grid[(y+1) % height][x] == '.':
        move_south.append((y,x))

  for (y,x) in move_south:
    grid[y][x] = '.'
    grid[(y+1) % height][x] = 'v'

  if len(move_east) == 0 and len(move_south) == 0:
    return False
  
  return True

def solve(grid):
  i = 1
  while move(grid):
    i += 1
  return i

# filename = "sample.txt"
filename = "input.txt"
grid = parse(filename)
print(solve(grid))