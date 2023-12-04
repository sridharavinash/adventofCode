import itertools
import re

def process_input_file(filename):
  for l in open(filename):
    line = l.strip()
    line = line.split(':')
    yield line

def part1(input):
  r = 12
  g = 13
  b = 14
  impossible = False
  pg = []
  # regex to parse 3 blue, 2 green, 1 red with named matches etc
  # continue till end of line
  rb = re.compile(r'(?P<blue>\d+) blue|(?P<green>\d+) green|(?P<red>\d+) red')

  for gm,s in input:
    gid = int(gm.split(' ')[1])
    s = s.strip()
    ss = s.split(';')
    ss = [s.strip() for s in ss]
    for t in ss:
      red = 0
      green = 0
      blue = 0
      if t == '': continue
      for m in rb.finditer(t):
        groups = m.groupdict(default='0')
        blue += int(groups['blue'])
        green += int(groups['green'])
        red += int(groups['red'])
      print(gid, red, green, blue)        
      if red > r or green > g or blue > b:
        impossible = True
        break
    if not impossible:
      pg.append(gid)
    else:
      impossible = False
  print(pg)
  print(sum(pg))


def part2(input):
  pg = []
  # regex to parse 3 blue, 2 green, 1 red with named matches etc
  # continue till end of line
  rb = re.compile(r'(?P<blue>\d+) blue|(?P<green>\d+) green|(?P<red>\d+) red')

  for gm,s in input:
    gid = int(gm.split(' ')[1])
    s = s.strip()
    ss = s.split(';')
    ss = [s.strip() for s in ss]
    gs = {'red': [], 'green': [], 'blue': []}
    for t in ss:
      red = 0
      green = 0
      blue = 0
      if t == '': continue
      for m in rb.finditer(t):
        groups = m.groupdict(default='0')
        blue += int(groups['blue'])
        green += int(groups['green'])
        red += int(groups['red'])
      print(gid, red, green, blue)        
      gs['red'].append(red)
      gs['green'].append(green)
      gs['blue'].append(blue)
    pg.append(max(gs['red']) * max(gs['green']) * max(gs['blue']))
  print(pg)
  print(sum(pg))


if __name__ == "__main__":
  inp = process_input_file("input.txt")
  #part1(inp)
  part2(inp)
