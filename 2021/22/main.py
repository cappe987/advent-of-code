
def parse_line(s):
  action, rest = s.rstrip().split(' ')
  xs, ys, zs = [a[2:].split('..') for a in rest.split(',')]
  x = [int(xs[0]), int(xs[1])]
  y = [int(ys[0]), int(ys[1])]
  z = [int(zs[0]), int(zs[1])]
  return Cube(x, y, z, True if action == "on" else False)

def parse(filename):
  return [parse_line(s) for s in open(filename)]

class Cube:
  def __init__(self, x, y, z, state):
    self.x = x
    self.y = y
    self.z = z
    self.state = state

  def overlap(self, other):
    if other.x[0] > self.x[1] or self.x[0] > other.x[1]:
      return None
    if other.y[0] > self.y[1] or self.y[0] > other.y[1]:
      return None
    if other.z[0] > self.z[1] or self.z[0] > other.z[1]:
      return None

    x_min = max(self.x[0], other.x[0])
    x_max = min(self.x[1], other.x[1])

    y_min = max(self.y[0], other.y[0])
    y_max = min(self.y[1], other.y[1])

    z_min = max(self.z[0], other.z[0])
    z_max = min(self.z[1], other.z[1])

    new_cube = Cube([x_min, x_max], [y_min, y_max], [z_min, z_max], True)
    return new_cube

  def volume(self):
    return (abs(self.x[1] - self.x[0]) + 1) * (abs(self.y[1] - self.y[0]) + 1) * (abs(self.z[1] - self.z[0]) + 1)


def solve(cubes, part1):

  processed = [] 
  for cube in cubes:
    if part1 and (cube.x[0] < -50 or cube.x[1] > 50 or cube.y[0] < -50 or cube.y[1] > 50 or cube.z[0] < -50 or cube.z[1] > 50):
      continue
    new_cubes = []
    for other in processed:
      new = other.overlap(cube)
      if new:
        if other.state == cube.state:
          new.state = not cube.state
        else:
          if other.state:
            new.state = False
          else:
            new.state = True
        new_cubes.append(new)
    
    if cube.state:
      processed.append(cube)
    processed += new_cubes

  vol = 0
  for cube in processed:
    if cube.state:
      vol += cube.volume()
    else:
      vol -= cube.volume()

  return vol
      
filename = "input.txt"
data = parse(filename)

print(solve(data, True))
print(solve(data, False))