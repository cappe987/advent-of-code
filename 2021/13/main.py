

def parse(filename):
  dots = []
  folds = []
  isfold = False
  for line in open(filename):
    if not isfold and line != "\n":
      dots.append([int(x) for x in line.split(',')])
    elif line == "\n":
      isfold = True
    else: 
      along = line.split()[2].split("=")
      folds.append((along[0], int(along[1])))
  return (dots, folds)

def print_grid(grid, ylen, xlen):
  for y in range(ylen):
    for x in range(xlen):
      print(str(grid[y][x]).ljust(3), end='')
    print()

def make_grid(dots):
  ylen = max(map(lambda xy: xy[1], dots)) + 1
  xlen = max(map(lambda xy: xy[0], dots)) + 1
  grid = []
  for y in range(ylen):
    row = []
    for x in range(xlen):
      row.append(0)
    grid.append(row)
  
  for dot in dots:
    grid[dot[1]][dot[0]] += 1

  return (grid, ylen, xlen)


def fold(grid, ylen, xlen, axis, along):
  if axis == "y":
    for y in range(along+1, ylen):
      for x in range(xlen):
        grid[along-(y-along)][x] += grid[y][x]
    return (along, xlen)
  elif axis == "x":
    for y in range(ylen):
      for x in range(along+1, xlen):
        grid[y][along-(x-along)] += grid[y][x]
    return (ylen, along)

def count(grid, ylen, xlen):
  total = 0
  for y in range(ylen):
    for x in range(xlen):
      if grid[y][x] > 0:
        total += 1
  return total

def solve_1(filename):
  dots, folds = parse(filename)
  grid, ylen, xlen = make_grid(dots)
  ylen, xlen = fold(grid, ylen, xlen, folds[0][0], folds[0][1])
  print(count(grid, ylen, xlen))

def solve_2(filename):
  dots, folds = parse(filename)
  grid, ylen, xlen = make_grid(dots)
  for f in folds:
    ylen, xlen = fold(grid, ylen, xlen, f[0], f[1])
  print_grid(grid, ylen, xlen)

filename = "input.txt"
solve_1(filename)
solve_2(filename)



