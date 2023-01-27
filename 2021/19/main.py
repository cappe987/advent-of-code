

def parse_probe(line):
  x = line.split(',')
  return (int(x[0]), int(x[1]), int(x[2]))

def parse(filename):
  data = open(filename).readlines()
  scanners = []
  probes = []
  i = 0
  for line in data:
    if "scanner" in line:
      continue
    elif line == '\n':
      scanners.append((i, probes))
      probes = []
      i += 1
    else:
      probes.append(parse_probe(line))
  return scanners


rotations = [ # x is facing x
  lambda x,y,z: (x, y, z),
  lambda x,y,z: (x, -z, y),
  lambda x,y,z: (x, -y, -z),
  lambda x,y,z: (x, z, -y),
  lambda x,y,z: (-x, -y, z), # x is facing -x
  lambda x,y,z: (-x, -z, -y),
  lambda x,y,z: (-x, y, -z),
  lambda x,y,z: (-x, z, y),
  lambda x,y,z: (-z, x, -y), # x is facing y
  lambda x,y,z: (y, x, -z),
  lambda x,y,z: (z, x, y),
  lambda x,y,z: (-y, x, z),
  lambda x,y,z: (z, -x, -y), # x is facing -y
  lambda x,y,z: (y, -x, z),
  lambda x,y,z: (-z, -x, y),
  lambda x,y,z: (-y, -x, -z),
  lambda x,y,z: (-y, -z, x), # x is facing z
  lambda x,y,z: (z, -y, x),
  lambda x,y,z: (y, z, x),
  lambda x,y,z: (-z, y, x),
  lambda x,y,z: (z, y, -x), # x is facing -z
  lambda x,y,z: (-y, z, -x),
  lambda x,y,z: (-z, -y, -x),
  lambda x,y,z: (y, -z, -x)
]

def add_to_map(m, scanner):
  for coords in scanner:
    if coords in m:
      m[coords] += 1
    else:
      m[coords] = 1
    
def add_tup(a,b):
  return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def calc_offset(xyz1, xyz2):
  return (xyz1[0] - xyz2[0], xyz1[1] - xyz2[1], xyz1[2] - xyz2[2])

def tryMatch(m, scanner):
  for c1 in m:
    for c2 in scanner:
      i = 0
      for rotate in rotations:
        overlaps = []
        offset = calc_offset(c1, rotate(c2[0], c2[1], c2[2]))
        for (x,y,z) in scanner:
          xyz = add_tup(rotate(x, y, z), offset)
          if xyz in m:
            overlaps.append(xyz)
        if len(overlaps) >= 12:
          return (True, i, overlaps, offset)
        i += 1
  return (False, None, None, None)
    
def print_id(unmatched):
  for scan in unmatched:
    print(scan[0], "", end='')
  print()

def match_positions(i, beacons, offset):
  return [add_tup(rotations[i](x[0], x[1], x[2]), offset) for x in beacons]


def solve(scans):
  m = dict()
  matched = [scans[0]]
  unmatched = scans[1:]
  add_to_map(m, scans[0][1])
  scanners = []
  while len(unmatched) > 0:
    scan = unmatched[0]
    (res, i, overlaps, offset) = tryMatch(m, scan[1])
    unmatched.remove(scan)
    if res:
      add_to_map(m, match_positions(i, scan[1], offset))
      matched.append(scan)
      print("Matched", scan[0])
      scanners.append(offset)
    else:
      unmatched.append(scan)

  return len(m), scanners

def manhat(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1] + abs(a[2] - b[2]))

def solve_2(coordinates):
  high = 0
  for i in range(len(coordinates)):
    for j in range(len(coordinates)):
      high = max(high, manhat(coordinates[i], coordinates[j]))
  
  return high

# filename = "sample.txt"
filename = "input.txt"
data = parse(filename)
res, scanners = solve(data)
print(res)
print(solve_2(scanners))
    