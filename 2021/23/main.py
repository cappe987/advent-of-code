
# I solved this whole day by hand.
# The solution below works for part 1
# but not for part 2 and I'm too lazy
# to debug it for now.

#############
#...........#
###B#B#C#D###
  #D#C#B#A#
  #D#B#A#C#
  #D#C#A#A#
  #########

roompos = [2, 4, 6, 8]
corridor_positions = [0,1,3,5,7,9,10]

def multiplier(amphipod, cost):
  if amphipod == 0:
    return cost
  elif amphipod == 1:
    return cost * 10
  elif amphipod == 2:
    return cost * 100
  elif amphipod == 3:
    return cost * 1000

def enter_cost(corridor, pos, rooms, roomnr, part1):
  amphipod = roomnr
  if len(rooms[roomnr]) > 0 and any(map(lambda amph: amph != amphipod, rooms[roomnr])):
    return False, -1 # Others still in that room
  if len(rooms[roomnr]) == (2 if part1 else 4):
    return False, -1
  
  if pos > roompos[roomnr]:
    r = list(range(roompos[roomnr], pos))
  else:
    r = list(range(pos+1, roompos[roomnr]+1))
  for i in r:
    if corridor[i] != -1:
      return False, -1 # Path blocked

  cost = len(r) + (2 - len(rooms[roomnr]) if part1 else 4 - len(rooms[roomnr]))
  # Cost of moving from corridor to the bottom of room
  return True, multiplier(amphipod, cost)

def leave_cost(corridor, target, rooms, roomnr, part1):
  if len(rooms[roomnr]) == 0:
    return False, -1
  if all(map(lambda amph: amph == roomnr, rooms[roomnr])):
    return False, -1

  # Cost of leaving the room
  if target > roompos[roomnr]:
    r = list(range(roompos[roomnr]+1, target+1))
  else:
    r = list(range(target, roompos[roomnr]))
  for i in r:
    if corridor[i] != -1:
      return False, -1 # Path blocked

  cost = len(r) + (3 - len(rooms[roomnr]) if part1 else 5 - len(rooms[roomnr]))
  return True, multiplier(rooms[roomnr][0], cost)

def is_done(rooms, part1):
  for nr in range(4):
    if len(rooms[nr]) == (2 if part1 else 4):
      for i in rooms[nr]:
        if i != nr:
          return False
    else:
      return False
  return True
  
def bfs(corridor, rooms, cost, low, part1, cache):
  mem = (tuple(corridor), tuple(tuple(r) for r in rooms))
  if mem in cache:
    return min(cache[mem], low)
  if cost >= low:
    return low
  elif is_done(rooms, part1):
    print("DONE", corridor, rooms, cost)
    return cost

  # Move out of room
  for roomnr in range(4):
    if len(rooms[roomnr]) > 0:
      for pos in corridor_positions: 
        res, _cost = leave_cost(corridor, pos, rooms, roomnr, part1)
        if res:
          cr = corridor
          rs = rooms
          cr[pos] = rs[roomnr][0]
          del rs[roomnr][0]
          __cost = bfs(cr, rs, cost + _cost, low, part1, cache)
          rs[roomnr].insert(0, cr[pos])
          cr[pos] = -1
          cache[(tuple(cr), tuple(tuple(r) for r in rs))] = __cost
          if __cost < low:
            low = __cost

  # Move into rooms
  for pos in corridor_positions:
    if corridor[pos] != -1:
      res, _cost = enter_cost(corridor, pos, rooms, corridor[pos], part1)
      if res:
        cr = corridor
        rs = rooms
        amphi = cr[pos]
        rs[amphi].insert(0, amphi)
        cr[pos] = -1
        __cost = bfs(cr, rs, cost + _cost, low, part1, cache)
        cr[pos] = rs[amphi][0]
        cache[(tuple(cr), tuple(tuple(r) for r in rs))] = __cost
        del rs[amphi][0]
        if __cost < low:
          low = __cost
  
  return low


corridor = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

rooms_p1 = [[1, 3], [1, 2], [2, 0], [3, 0]]
rooms_p2 = [[1, 3, 3, 3], [1, 2, 1, 2], [2, 1, 0, 0], [3, 0, 2, 0]]
cache = dict()

print(bfs(corridor, rooms_p2, 0, float('inf'), False, cache)) # Wrong answer
