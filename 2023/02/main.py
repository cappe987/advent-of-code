import sys
sys.path.append('../')
from aoclib import *

data = open("example.txt").readlines()
data = open("input.txt").readlines()

def parse(line):
    game, grabs = line.split(': ')
    gameid = int(game[5:])

    rounds = []
    for round in grabs.split('; '):
        r = [0,0,0]
        cindex = {'red': 0, 'green': 1, 'blue': 2}
        color = round.split(', ')
        for x in color:
            num, c = x.split(' ')
            r[cindex[c.strip()]] = int(num)
        rounds.append(r)

    return gameid, rounds

def part_2(rounds):
    red = max(map(lambda x: x[0], rounds))
    green = max(map(lambda x: x[1], rounds))
    blue = max(map(lambda x: x[2], rounds))
    return red * green * blue

games = list(map(parse, data))
valid_games = filter(lambda x: all(map(lambda y: y[0] <= 12 and y[1] <= 13 and y[2] <= 14, x[1])), games)

print(f"Part 1: {sum(map(lambda y: y[0], valid_games))}")
print(f"Part 2: {sum(map(lambda y: part_2(y[1]), games))}")
