import itertools

def process_input_file(filename):
  for l in open(filename):
    line = l.strip()
    yield int(line)

def part1(input):
  prev = -1
  inc = 0
  for i in input:
    if prev == -1:
      print(f'{i} (n/a)')
      prev = i
      continue
    if i > prev:
      print(f'{i} (increase)')
      inc += 1
    else:
      print(f'{i} (decrease)')
    prev = i
  return inc

def part2(input):
  acc = []
  prev = -1
  inc = 0
  for i in input:
    acc.append(i)
    if len(acc) % 3 == 0:
      if prev == -1:
        prev = sum(acc)
        acc.pop(0)
        continue
      elif sum(acc) > prev:
        inc+=1
        print(f'{sum(acc)} (increase)')
      prev = sum(acc)
      acc.pop(0)
  return inc
    
if __name__ == "__main__":
  inp = process_input_file("input.txt")
  #print(part1(inp))
  print(part2(inp))
