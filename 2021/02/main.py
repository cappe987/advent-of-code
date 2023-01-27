

def parse(s):
    a = s.split()
    return (a[0], int(a[1]))

data = list(map(parse, open("input.txt").readlines()))


hori = 0
depth = 0

for (s, X) in data:
    if s == "forward":
        hori += X
    elif s == "down":
        depth += X
    elif s == "up":
        depth -= X

print(hori*depth)


# Part 2
hori = 0
depth = 0
aim = 0

for (s, X) in data:
    if s == "forward":
        hori += X
        depth += (aim * X)
    elif s == "down":
        aim += X
    elif s == "up":
        aim -= X


print(hori*depth)
