

data = list(map(int, open("input.txt").readlines()))

prev = data[0]
count = 0

for x in data:
    if x > prev:
        count += 1
    prev = x

print(count)


# Part 2

sumA = data[0] + data[1]
sumB = data[1]
sumC = 0
prev = 0
count = 0

for i in range(2, len(data)):
    sumA += data[i]
    sumB += data[i]
    sumC += data[i]

    if sumA > prev and i != 2:
        count += 1

    prev = sumA
    sumA = sumB
    sumB = sumC
    sumC = 0


print(count)

