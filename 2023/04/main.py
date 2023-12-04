import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def get_score(m):
    return 0 if m == 0 else 2**(m-1)

def calc_score(games):
    matches = [sum([(1 if num in game[0] else 0) for num in game[1]]) for game in games]

    cards = [1 for _ in games]
    for i,m in enumerate(matches):
        for n in range(m):
            cards[i+n+1] += cards[i]

    return sum(map(get_score, matches)), sum(cards)

data = map(lambda x: x.split(': ')[1], data)
data = list(map(lambda x: [list(map(int, y.split())) for y in x.split(' | ')], data))
res = calc_score(data)
print(f"Part 1: {res[0]}")
print(f"Part 2: {res[1]}")
