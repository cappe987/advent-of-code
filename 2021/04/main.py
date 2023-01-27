

def fm(s):
  return (int(s), False)

def parse(file):
  data = open(file).readlines()
  nums = list(map(int, data[0].split(',')))
  boards = []

  i = 2
  while i < len(data):
    b = []
    b.append(list(map(fm, data[i+0].split())))
    b.append(list(map(fm, data[i+1].split())))
    b.append(list(map(fm, data[i+2].split())))
    b.append(list(map(fm, data[i+3].split())))
    b.append(list(map(fm, data[i+4].split())))
    i += 6
    boards.append(b)
  return (boards, nums)

def mark(boards, num):
  for b in boards:
    for i in range(5):
      for j in range(5):
        if b[i][j][0] == num:
          b[i][j] = (num, True)

def checkBoard(b):
  for row in range(5):
    for col in range(5):
      if b[row][col][1] == False:
        break
    else:
      return True

  for col in range(5):
    for row in range(5):
      if b[row][col][1] == False:
        break
    else:
      return True
  return False

def play(boards, nums, played_nums, part1):
  for n in nums:
    to_remove = []
    mark(boards, n)
    played_nums.append(n)
    for bi in range(len(boards)):
      if checkBoard(boards[bi]):
        if part1:
          return boards[bi]
        else:
          to_remove.append(boards[bi])
    for b in to_remove:
      if len(boards) > 1:
        boards.remove(b)
      else:
        return boards[0]

def sumUnmarked(b):
  total = 0
  for row in b:
    for loc in row:
      if not loc[1]:
        total += loc[0]
  return total


boards, nums = parse("input.txt")
played_nums = []
winner = play(boards, nums, played_nums, True)
tot = sumUnmarked(winner)
print(tot * played_nums[-1])

boards, nums = parse("input.txt")
played_nums = []
winner = play(boards, nums, played_nums, False)
tot = sumUnmarked(winner)
print(tot * played_nums[-1])




