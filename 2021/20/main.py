

def parse(filename):
  data = open(filename).readlines()
  algo = ["1" if x == "#" else "0" for x in data[0].rstrip()]

  grid = [x.rstrip() for x in data[2:]]
  size = (0, len(grid)-1)
  pixels = dict()
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      pixels[(i,j)] = "1" if grid[i][j] == "#" else "0"

  return pixels, size, algo


def print_grid(pixels, size):
  for i in range(size[0], size[1]):
    for j in range(size[0], size[1]):
      print("#" if pixels[(i,j)] == "1" else ".", end='')
    print()


def get_square(x,y):
  return [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x, y), (x, y+1), (x+1,y-1), (x+1,y), (x+1, y+1)]

def get_binary(pixels, algo, i, j, voidflip):
  binary = ""
  for (x,y) in get_square(i,j):
    if (x,y) not in pixels:
      binary += "1" if voidflip else "0"
    else:
      binary += pixels[(x,y)]
  return binary

def enhance(pixels, size, algo, voidflip):
  np = dict()
  size = (size[0]-1, size[1]+1)
  for i in range(size[0], size[1]+1):
    for j in range(size[0], size[1]+1):
      binary = get_binary(pixels, algo, i, j, voidflip)
      np[(i,j)] = algo[int(binary, 2)]
  return (np, size)

def solve(pixels, size, algo):
  pixels, size = enhance(pixels, size, algo, False)
  pixels, size = enhance(pixels, size, algo, True)
  return pixels, size

def solve_2(pixels, size, algo):
  voidflip = False
  for _ in range(50):
      pixels, size = enhance(pixels, size, algo, voidflip)
      voidflip = not voidflip

  return pixels, size

def count(pixels):
    tot = 0
    for p in pixels:
        if pixels[p] == "1":
            tot += 1
    return tot

filename = "sample.txt"
filename = "input.txt"

pixels, size, algo = parse(filename)
pixels, size = solve(pixels, size, algo)
print(count(pixels)) # 5461

pixels, size, algo = parse(filename)
pixels, size = solve_2(pixels, size, algo)
print(count(pixels)) # 18226

