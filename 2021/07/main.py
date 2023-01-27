

def calc_fuel(target, crabs):
  tot = 0
  for c in crabs:
    if c < target:
      tot += (target - c)
    else:
      tot += (c - target)
  return tot

def calc_fuel_2(target, crabs):
  tot = 0
  for c in crabs:
    if c < target:
      tot += sum(range(1, (target - c)+1))
    else:
      tot += sum(range(1, (c - target)+1))
  return tot

def solve(crabs, calc_fuel):
  low = 9999999999
  for i in range(min(crabs), max(crabs)+1):
    low = min(low, calc_fuel(i, crabs))

  print(low)

# data = list(map(int, open("sample.txt").read().split(",")))
data = list(map(int, open("input.txt").read().split(",")))

solve(data, calc_fuel)
solve(data, calc_fuel_2)
