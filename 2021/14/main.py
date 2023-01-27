from collections import defaultdict

def parse(filename):
  data = list(map(lambda x: x.rstrip(), open(filename).readlines()))

  rules = dict()
  for rule in data[2:]:
    rules[rule[0:2]] = rule[6]

  count = defaultdict(lambda: 0)
  for c in data[0]:
    count[c] += 1


  pairs = defaultdict(lambda: 0)
  s = data[0]
  for i in range(len(s)-1):
    pairs[s[i]+s[i+1]] += 1


  return (count, pairs, rules)


def apply(count, pairs, rules):
  for (p,val) in list(pairs.items()):
    c = rules[p]
    count[c] += val
    pairs[p] -= val
    pairs[p[0] + c] += val
    pairs[c + p[1]] += val


def solve(filename, lim):
  count, pairs, rules = parse(filename)
  for _ in range(lim):
    apply(count, pairs, rules)
    
  low = 999999999999
  high = 0
  for c,v in count.items():
    low = min(low, v)
    high = max(high, v)

  print(high-low)



# filename = "sample.txt"
filename = "input.txt"
solve(filename, 10)
solve(filename, 40)
