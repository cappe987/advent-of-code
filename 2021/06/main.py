


def part2(school):
  birth = [0]*270
  for x in range(8):
    newcount = 0
    for i in range(len(school)):
      if school[i] == 0:
        school[i] = 6
        newcount += 1
      else:
        school[i] -= 1
    birth[x] = newcount

  total = len(school)
  for i in range(256):
    new = birth[i]
    total += new
    birth[i+7] += birth[i]
    birth[i+9] += new
  
  return total

def part1(school):
  for _ in range(80):
    newcount = 0
    for i in range(len(school)):
      if school[i] == 0:
        school[i] = 6
        newcount += 1
      else:
        school[i] -= 1

    for i in range(newcount):
      school.append(8)
  return len(school)
      


# data = list(map(int, open("sample.txt").read().split(",")))
data = list(map(int, open("input.txt").read().split(",")))
print(part1(data))
data = list(map(int, open("input.txt").read().split(",")))
print(part2(data))