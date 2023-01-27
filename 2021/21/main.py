from functools import lru_cache

def sample_input():
  return (4, 8)

def real_input():
  return (6, 4)


def gen_die():
  die = 0
  while True:
    die += 1
    if die > 100:
      die = 1
    yield die



def play(p1, p2):
  lim = 1000
  die = gen_die()
  throws = 0
  p1_score = 0
  p2_score = 0
  p1 -= 1
  p2 -= 1
  while True:
    moves = next(die) + next(die) + next(die)
    throws += 3
    p1 = p1 + moves
    p1 = p1 % 10
    p1_score += p1 + 1
    if p1_score >= lim:
      return p2_score * throws
    
    moves = next(die) + next(die) + next(die)
    throws += 3
    p2 = p2 + moves
    p2 = p2 % 10
    p2_score += p2 + 1
    if p2_score >= lim:
      return p1_score * throws


def sub(inp):
  return (inp[0] - 1, inp[1] - 1)
     
@lru_cache(maxsize=100000)
def play_2(p1, p2, p1_score, p2_score, p1_turn):
  if p1_score >= 21:
    return (1, 0) 
  elif p2_score >= 21:
    return (0, 1)

  tot = (0,0)
  for i in range(1,4):
    for j in range(1,4): 
      for k in range(1,4): 
        if p1_turn:
          pos = (p1 + i+j+k) % 10
          res = play_2(pos, p2, p1_score + pos + 1, p2_score, False)
        else: 
          pos = (p2 + i+j+k) % 10 
          res = play_2(p1, pos, p1_score, p2_score + pos + 1, True) 
        tot = (tot[0] + res[0], tot[1] + res[1]) 
  return tot

print(play(*real_input()))
print(max(play_2(*sub(real_input()), 0, 0, True)))



