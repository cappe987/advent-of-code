from collections import defaultdict

def print_matrix(m):
  for row in m:
    print(row)

def is_big(a):
  return a.isupper()

def parse(filename):
  lines = [x.rstrip().split('-') for x in open(filename)]

  d = defaultdict(lambda: list())
  for (a,b) in lines:
    d[a].append(b)
    d[b].append(a)

  return d

def has_double_small(path):
  di = defaultdict(lambda: 0)
  for cave in path:
    if not is_big(cave):
      if di[cave] == 1:
        return True
      di[cave] += 1
  return False

def traverse(d, cave, path, part1):
  if cave == "end":
    return [path]
  res = []

  for neigh in d[cave]:
    if neigh == "start":
      continue
    if not is_big(neigh) and neigh in path and (part1 or has_double_small(path)):
      continue
    ls = traverse(d, neigh, path[:] + [neigh], part1)
    if ls:
      res.extend(ls)

  return res

def solve(d, part1):
  
  return len(traverse(d, "start", ["start"], part1))

d = parse("input.txt")
print(solve(d, True))
print(solve(d, False))

