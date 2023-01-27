from collections import defaultdict

def parse(filename):
  data = open(filename).read()[13:].split(", ")
  xr = data[0][2:].split("..")
  yr = data[1][2:].split("..")
  return ((int(xr[0]), int(xr[1])), (int(yr[0]), int(yr[1])))

def in_range(x,y, data):
  return x >= data[0][0] and x <= data[0][1] and y >= data[1][0] and y <= data[1][1]

def throw(vx, vy, data):
  x = 0
  y = 0
  high = -99999
  while x <= data[0][1] and y >= data[1][0]:
    x += vx
    y += vy 
    vx = vx - 1 if vx > 0 else 0
    vy -= 1
    high = max(high, y)
    if in_range(x, y, data):
      return True, high
  return False, (x,y)
      
def shoot(data):
  high = -99999
  hits = []
  for vx in range(500):
    for vy in range(-500, 500):
      res, val = throw(vx, vy, data)
      if res:
        hits.append((vx, vy))
        if val > high:
          high = val
  
  return high, len(hits)

# filename = "sample.txt"
filename = "input.txt" 
data = parse(filename)

print(shoot(data))