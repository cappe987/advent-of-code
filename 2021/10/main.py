

syntax_scoring = {
  ')' : 3,
  ']' : 57,
  '}' : 1197,
  '>' : 25137
}

completion_scoring = {
  ')' : 1,
  ']' : 2,
  '}' : 3,
  '>' : 4
}

def parse(filename):
  return open(filename).readlines()

def syntax_check(line, complete):
  while line and line[0] in ['(', '[', '{', '<']:
    if line[0] == '(':
      line = syntax_check(line[1:], complete)
      if not line:
        complete.append(')')
      elif line[0] != ')':
        raise KeyError(line[0])
      else:
        line = line[1:]
    elif line[0] == '[':
      line = syntax_check(line[1:], complete)
      if not line:
        complete.append(']')
      elif line[0] != ']':
        raise KeyError(line[0])
      else:
        line = line[1:]
    elif line[0] == '{':
      line = syntax_check(line[1:], complete)
      if not line:
        complete.append('}')
      elif line[0] != '}':
        raise KeyError(line[0])
      else:
        line = line[1:]
    elif line[0] == '<':
      line = syntax_check(line[1:], complete)
      if not line:
        complete.append('>')
      elif line[0] != '>':
        raise KeyError(line[0])
      else:
        line = line[1:]

  return line
    

def solve(lines):
  syntax_score = 0
  completion_scores = []
  for line in lines:
    completion = []
    line = line.rstrip()
    try:
      syntax_check(line, completion)
      score = 0
      for c in completion:
        score *= 5
        score += completion_scoring[c]
      completion_scores.append(score)
    except KeyError as e:
      syntax_score += syntax_scoring[e.args[0]]

  completion_scores.sort()

  return (syntax_score, completion_scores[len(completion_scores)//2])


# data = parse("sample.txt")
data = parse("input.txt")
print("Answer:", *solve(data))