import itertools

def process_input_file(filename):
  for l in open(filename):
    inst, v = l.strip().split()
    yield inst,int(v)

def part1(input):
  h = 0
  d = 0
  for inst, v in input:
    if inst == "forward":
      h += v
    elif inst == "down":
      d += v
    elif inst == "up":
      d -= v
  return h * d

def part2(input):
  h = 0
  d = 0
  aim = 0
  for inst, v in input:
    if inst == "forward":
      h += v
      d += aim * v
    elif inst == "down":
      aim += v
    elif inst == "up":
      aim -= v
  return h * d

if __name__ == "__main__":
  inp = process_input_file("input.txt")
  #print(part1(inp))
  print(part2(inp))
