import json
import math


class Node:
  def __init__(self, data):
    if isinstance(data, list):
      self.left  = Node(data[0])
      self.right = Node(data[1])
      self.val   = None
    else:
      self.left  = None
      self.right = None
      self.val   = data
  
  def __add__(n1, n2):
    res = red_all(Node([to_list(n1), to_list(n2)]))
    return res

  def __eq__(n1, n2):
    if n1 and not n2 or n2 and not n1:
      return False
    if n1.val != None and n2.val != None and n1.val == n2.val:
      return True
    l = False
    r = False
    if n1.left and n2.left:
      l = n1.left == n2.left
    if n1.right and n2.right:
      r = n1.right == n2.right
    return l and r

    
def magnitude(node):
  if node.val != None:
    return node.val
  return 3 * magnitude(node.left) + 2 * magnitude(node.right)

def to_list(node):
  if node.val != None:
    return node.val
  else:
    l = to_list(node.left)
    r = to_list(node.right)
    return [l, r]

def parse(filename):
  return [Node(json.loads(x)) for x in open(filename).readlines()]

def find_rightmost(node):
  if node.right:
    return find_rightmost(node.right)
  else:
    return node

def find_leftmost(node):
  if node.left:
    return find_leftmost(node.left)
  elif node.val != None:
    return node
  else:
    return None

def reduce_num(node, depth, checkExp):
  if depth == 4 and node.val == None and checkExp: # Explode
    return "explode", (node.left.val, node.right.val, node)
  elif node.val and node.val >= 10 and not checkExp: # Split
    return "split", Node([node.val//2, math.ceil(node.val/2)])
  elif node.val != None:
    return "cont", None



  res, val = reduce_num(node.left, depth + 1, checkExp)
  if res == "explode":
    (l, r, nd) = val
    if r != None:
      n = find_leftmost(node.right)
      if n:
        n.val += r
      else:
        raise Exception("No Right found " + str(to_list(node)))
    if l == None:
      return "done", nd
    return "explode", (l, None, nd)
  elif res == "split":
    if val == None:
      return res, val
    node.left = val
    return "split", None
  elif res == "done":
    return "done", val

  res, val = reduce_num(node.right, depth + 1, checkExp)
  if res == "explode":
    (l, r, nd) = val
    if l != None:
      n = find_rightmost(node.left)
      if n:
        n.val += l
      else:
        raise Exception("No Left found " + str(to_list(node)))
    if r == None:
      return "done", nd
    return "explode", (None, r, nd)
  elif res == "split":
    if val == None:
      return res, val
    node.right = val
    return "split", None
  elif res == "done":
    return "done", val

  return "cont", None


def red(node, checkExp):
  res, val =  reduce_num(node, 0, checkExp)
  if res == "explode":
    (_, _, nd) = val
    if nd:
      nd.val = 0
      nd.left = None
      nd.right = None
  elif res == "done" and val != None:
    val.val = 0
    val.left = None
    val.right = None
  return node

def red_all(node):
  prev = Node(to_list(node))
  while True: # Explosions. Explode all at start
    node = red(node, True)
    if prev == node:
      break
    prev = Node(to_list(node))

  while True:
    node = red(node, False)
    node = red(node, True)
    if prev == node:
      break
    prev = Node(to_list(node))
    
  return node
  
def solve(nums):
  tot = nums[0]
  for num in nums[1:]:
    tot += num
  return magnitude(tot)

def solve_part2(nums):
  high = 0
  for i in range(len(nums)):
    for j in range(len(nums)):
      if i != j:
        val = nums[i] + nums[j]
        high = max(magnitude(val), high)
  return high

filename = "input.txt" 
nums = parse(filename)
print(solve(nums)) # 4469
print(solve_part2(nums)) # Takes a couple seconds, 4770

