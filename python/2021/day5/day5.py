import itertools
import re
a = {}
regex = r"(\d+)"
def process_input_file(filename):
  for l in open(filename):
    ll = re.findall(regex, l)
    line = [int(y) for y in  ll]
    yield line

def part1(input, p2=False):
  for x1,y1,x2,y2 in input:
    if y1 == y2:
      for i in range(min(x1,x2),max(x1,x2)+1):
        a[(i,y1)] = a.setdefault((i,y1),0) + 1 
    elif x2 == x1:
      for i in range(min(y1,y2),max(y1,y2)+1):
        a[(x1,i)] = a.setdefault((x1,i),0) + 1
    # part 2 
    else:
      m = int((y2-y1)/(x2-x1))
      # generate points on the line
      if(x1,y1) > (x2,y2):
        x = x1
        while x >= x2:
          y = m*(x-x1)+y1
          a[(x,y)] = a.setdefault((x,y),0) + 1
          if m < 0: x += m 
          else: x -= m
      else:
        x = x2
        while x >= x1:
          y = m*(x-x2)+y2
          a[(x,y)] = a.setdefault((x,y),0) + 1
          if m < 0: x += m 
          else: x -= m
  print(sum(1 for x in a.values() if x >= 2))

def part2(input):
  part1(input, True)

if __name__ == "__main__":
  inp = process_input_file("input.txt")
  part1(inp)
