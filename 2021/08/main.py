
def parseline(s):
  words = s.split()
  return (words[:10], words[11:])

def parse(filename):
  return list(map(parseline, open(filename).readlines()))



def mapping(word):
  if len(word) == 2:
    return {1: set(word)}
  elif len(word) == 4:
    return {4: set(word)}
  elif len(word) == 3:
    return {7: set(word)}
  elif len(word) == 7:
    return {8: set(word)}
  else:
    return None

def part_1(w):
  if len(w) == 2 or len(w) == 4 or len(w) == 3 or len(w) == 7:
    return 1
  else:
    return 0


def part_1_solve(line):
  return sum(map(part_1, line[1]))

def overlap(d, words):
  overlaps = dict()
  for word in words:
    overlaps[word] = [[], set(word)]
  for word in words:
    for k,v in d.items():
      if set(word) & v:
        overlaps[word][0].append(k)
        overlaps[word][1] = overlaps[word][1] & v
  return overlaps

def decode(line):
  d = dict()
  rm = []
  decoder = dict()
  for word in line[0]:
    m = mapping(word)
    if m != None:
      decoder[word] = list(m.keys())[0]
      d.update(m)
      rm.append(word)
  for i in rm:
    line[0].remove(i)

  
  overlaps = overlap(d, line[0])
  n039 = []
  n256 = []

  for k,v in overlaps.items():
    if len(v[1]) == 2:
      n039.append(k)
    elif len(v[1]) == 1:
      n256.append(k)

  for word in n039:
    if len(word) == 5:
      n3 = word

  overlaps = overlap({3:set(n3)}, list(filter(lambda x: x != n3, n039)))
  for k,v in overlaps.items():
    if len(v[1]) == 5:
      n9 = k
    elif len(v[1]) == 4:
      n0 = k
  
  for word in n256:
    if len(word) == 6:
      n6 = word
  
  n256.remove(n6)
  overlaps = overlap({9:set(n9)}, n256)
  for k,v in overlaps.items():
    if len(v[1]) == 5:
      n5 = k
    elif len(v[1]) == 4:
      n2 = k


  decoder.update({n0: 0, n3: 3, n9: 9, n2: 2, n5: 5, n6: 6})

  num = ""
  for word in line[1]:
    for k,v in decoder.items():
      if set(word) == set(k):
        num += str(v)
  
  print(num)

  return int(num)


def solve_1(data):
  return sum(map(part_1_solve, data))
  
def solve_2(data):
  return sum(map(decode, data))



# data = parse("sample1.txt")
# data = parse("sample.txt")
data = parse("input.txt")

# print(solve_1(data))
# print(data)
print(solve_2(data))
