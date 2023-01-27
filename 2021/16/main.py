from math import prod

def parse(filename):
    return "".join([bin(int(x, 16))[2:].zfill(4) for x in open(filename).read() if x != '\n'])

def parseS(s):
    return "".join([bin(int(x, 16))[2:].zfill(4) for x in s if x != '\n'])

def toInt(s):
    return int(s, 2)

def op(nums, typ):
    if typ == 0:
        return sum(nums)
    elif typ == 1:
        return prod(nums)
    elif typ == 2:
        return min(nums)
    elif typ == 3:
        return max(nums)
    elif typ == 5:
        return 1 if nums[0] > nums[1] else 0
    elif typ == 6:
        return 1 if nums[0] < nums[1] else 0
    elif typ == 7:
        return 1 if nums[0] == nums[1] else 0

def parse_packet(data, i):
    ver = toInt(data[i:i+3])
    typ = toInt(data[i+3:i+6])
    i += 6
    
    if typ == 4:
        num = ""
        while True:
            num += data[i+1:i+5]
            if data[i] == '0':
                i += 5
                break
            i += 5
        
        return (i, [ver], toInt(num))
    else:
        id = data[i]
        vers = [ver]
        nums = []
        if id == '0':
            length = toInt(data[i+1: i+16])
            i += 16
            lim = i + length
            while i < lim:
                (i, ver, num) = parse_packet(data, i)
                vers.extend(ver)
                nums.append(num)
            val = op(nums, typ)
        else:
            packets = toInt(data[i+1: i+12])
            i += 12
            for j in range(packets):
                (i, ver, num) = parse_packet(data, i)
                vers.extend(ver)
                nums.append(num)
            val = op(nums, typ)

        return (i, vers, val)

filename = "input.txt"
data = parse(filename)
res = parse_packet(data, 0)
print(sum(res[1]))
print(res[2])
