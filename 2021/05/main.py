from collections import defaultdict

def parse_pair(s):
  x = s.split(",")
  return (int(x[0]), int(x[1]))

def parse(filename):
  data = open(filename).readlines()
  data = map(lambda x: x.split(" -> "), data)
  return list(map(lambda xs: (parse_pair(xs[0]), parse_pair(xs[1])), data))

def comp(a, b):
  return -1 if a < b else 1 if a > b else 0

def get_range(pair, part1):
  start = pair[0]
  end = pair[1]
  out = [start]

  if part1 and start[0] != end[0] and start[1] != end[1]:
    return []

  xdir = lambda x: x+comp(end[0], start[0])
  ydir = lambda y: y+comp(end[1], start[1])

  while start != end:
    start = (xdir(start[0]), ydir(start[1]))
    out.append(start)
  return out

def solve(data, part1):
  d = defaultdict(lambda: 0)

  for pair in data:
    for point in get_range(pair, part1):
      d[point] += 1

  count = 0
  for v in d.values():
    if v > 1:
      count += 1
  return count

data = parse("input.txt")
# data = parse("sample.txt")

print(solve(data, True))
print(solve(data, False))
