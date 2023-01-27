def solve():
  data = [int(x) for x in open("input_mod2.txt")]
  nums = []
  for i in range(0, len(data), 3):
    nums.append(tuple(data[i:i+3]))

  res = []
  stack = []
  i = 0
  for (div, check, offset) in nums:
    if check > 0:
      # res.append(None)
      stack.append((i, offset))
    else:
      (j, offset_val) = stack.pop()
      res.append((i, j, offset_val + check))
    i += 1

  high = [0]*14
  low  = [0]*14

  for (idx, ref, offset) in res:
    if offset > 0:
      hi = 9 - offset
      lo = offset + 1
      high[ref] = hi
      high[idx] = 9
      low[ref] = 1
      low[idx] = lo
    elif offset < 0:
      hi = offset + 9
      lo = 1 + -offset
      high[ref] = 9
      high[idx] = hi
      low[idx] = 1
      low[ref] = lo
    
  print("".join(map(str, high)))
  print("".join(map(str, low)))

solve()
