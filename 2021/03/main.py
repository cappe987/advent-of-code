


def opp(x):
    if x == 1:
        return 0
    elif x == 0:
        return 1
    else:
        return x

def calc_most(data):
    most = []
    for i in range(len(data[0])):
        ones = 0 
        zeros = 0
        for num in data:
            if num[i] == "1":
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            most.append(1)
        elif ones == zeros:
            most.append(-1)
        else:
            most.append(0)

    return most

data = open("input.txt").readlines()
# data = open("sample.txt").readlines()
data = list(map(lambda x: x.rstrip(), data))

# Part 1

most = calc_most(data)
gamma = "".join(list(map(str, most)))
epsilon = "".join(list(map(lambda x: "1" if x == "0" else "0", gamma)))
print(int(gamma, 2) * int(epsilon,2))

# Part 2

data1 = data[:] 
data2 = data[:]

i = 0
while len(data1) > 1:
    most = calc_most(data1)
    data1 = list(filter(lambda num: int(num[i]) == most[i] or (num[i] == "1" and most[i] == -1), data1))
    i += 1

i = 0
while len(data2) > 1:
    most = calc_most(data2)
    data2 = list(filter(lambda num: int(num[i]) == opp(most[i]) or (num[i] == "0" and most[i] == -1), data2))
    i += 1

print(int(data1[0], 2) * int(data2[0], 2))
