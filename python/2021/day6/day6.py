import itertools
from os import terminal_size

def process_input_file(filename):
  for l in open(filename):
    line = ''.join(l.split(','))
    return [int(i) for i in line]

def part1(input):
  l = input[:]
  trials = 0
  while trials < 150:
    for i in range(len(l)):
      if l[i] - 1 < 0:
        l[i] = 6
        l.append(8)
        continue
      l[i] -= 1
    trials += 1
    print(f"{trials}, len={len(l)}")
  print()

def part2(input):
  l = input[:]
  trails = 150
  x = l[0]
  tt = [x+1]
  s = 1
  endd = False
  while endd == False:
    for i in tt:
      six = i + 7
      eights = i + 9
      print(f"\r{i}, {six}, {eights}, s={s}", end="")
      if six > trails and eights > trails:
        endd= True
        break
      s += 2
      if six < trails:
        tt.append(six)
      if eights < trails:
        tt.append(eights)
      tt = sorted(tt)
      tt.pop(0)
  print()
if __name__ == "__main__":
  inp = process_input_file("test.txt")
  part1(inp)
  part2(inp)
