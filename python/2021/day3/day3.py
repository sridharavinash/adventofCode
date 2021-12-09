import itertools

def process_input_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

def part1(input):
  xx = [''.join(chars) for chars in zip(*input)]
  g = ''
  for x in xx:
    ones = x.count('1')
    zeros = x.count('0')
    if ones > zeros:
      g += '1'
    else:
      g += '0'
  gr = int(g, 2)
  inv = int(''.join(str(1-int(x))for x in g), 2)
  return gr * inv

def part2(input):
  yy = input
  i = 0
  while len(yy) > 1:
    xx = [''.join(chars) for chars in zip(*yy)]
    ones = xx[i].count('1')
    zeros = xx[i].count('0')
    if ones > zeros:
      zz = [x for x in yy if x[i] == '1']
    elif zeros > ones:
      zz = [x for x in yy if x[i] == '0']
    else:
      zz = [x for x in yy if x[i] == '1']
    yy = zz
    i += 1
  o2 = int(yy[0], 2)
  
  yy = input
  i = 0
  while len(yy) > 1:
    xx = [''.join(chars) for chars in zip(*yy)]
    ones = xx[i].count('1')
    zeros = xx[i].count('0')
    if ones < zeros:
      zz = [x for x in yy if x[i] == '1']
    elif zeros < ones:
      zz = [x for x in yy if x[i] == '0']
    else:
      zz = [x for x in yy if x[i] == '0']
    yy = zz
    i += 1
  co2 = int(yy[0], 2)
  return o2 * co2

if __name__ == "__main__":
  inp = process_input_file("input.txt")
  #print(part1(inp))
  print(part2(inp))
