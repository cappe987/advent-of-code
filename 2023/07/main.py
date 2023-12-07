import sys
sys.path.append('../')
from aoclib import *
from collections import Counter

data = open("example.txt").read()
data = open("input.txt").read()

def get_type(hand, p2):
    c = Counter(hand)
    if p2: # Replace jokers with most common
        jokers = c['0']
        if jokers == 5:
            return 6
        del c['0']
        high = c.most_common()[0]
        c[high[0]] += jokers

    if len(c) == 1: # Five-of-a-kind
        return 6
    elif len(c) == 2: # Full-house or four-of-a-kind
        for val in c.values():
            if val == 4: # Four-of-a-kind
                return 5
        return 4 # Full-house
    elif len(c) == 3: # Three-of-a-kind or two-pairs
        for val in c.values():
            if val == 3:
                return 3 # Three-of-a-kind
        return 2 # Two-pairs
    elif len(c) == 4: # One-pair
        return 1
    else: # High-card
        return 0

def solve(data, p2):
    if p2: # Jokers are now last
        data = map(lambda x: (x[0].replace("C", "0"), x[1]), data)

    data = list(map(lambda x: (get_type(x[0], p2), x[0], x[1]), data))
    data.sort()

    res = 0
    for i,hand in enumerate(data, 1):
        res += i * hand[2]
    return res

# So strings can be sorted alphabetically when they have the same type
data = data.replace("T", "B")
data = data.replace("J", "C")
data = data.replace("Q", "D")
data = data.replace("K", "E")
data = data.replace("A", "F")
data = data.split('\n')[:-1]
data = list(map(lambda x: (x[:5],int(x[5:])), data))

print(f"Part 1: {solve(data, False)}")
print(f"Part 2: {solve(data, True)}")
