import itertools
import re

def process_input_file(filename):
  for l in open(filename):
    line = l.strip()
    yield line

def part1(input):
  i =0
  # regex match numbers
  rg = re.compile(r'\d+')
  rs = re.compile(r'[^\w\s\.]')
  nm = {}
  ns = []
  for line in input:
    for mrs in rs.finditer(line):
      print(mrs.start(), mrs.end())
      idx = mrs.start()
      ns.append((i,idx+1))
      ns.append((i,idx-1))
      ns.append((i-1,idx))
      ns.append((i-1,idx+1))
      ns.append((i-1,idx-1))
      ns.append((i+1,idx))
      ns.append((i+1,idx+1))
      ns.append((i+1,idx-1))
    # get the index of each match
    for m in rg.finditer(line):
      n = m.start()
      nm[((i,n), m.group())] = []
      # record the index of each match
      for j in range(m.end()-m.start()):
        nm[(i,n), m.group()].append((i, n+j))
    i += 1
  ret = []
  for num in nm.items():
    for n in num[1]:
      if n in ns:
        print(num[0], n)
        ret.append(int(num[0][1]))
        break
  print(ret)
  print(sum(ret))

def part2(input):
  i =0
  # regex match numbers
  rg = re.compile(r'\d+')
  rs = re.compile(r'\*')
  nm = {}
  for line in input:
    # get the index of each match
    for m in rg.finditer(line):
      n = m.start()
      # record the index of each match
      for j in range(m.end()-m.start()):
        nm[(i,n+j)] = m.group()
    i += 1
  ret = []
  # reset line iter
  input = process_input_file("test.txt")
  i = 0
  for line in input:
    for mrs in rs.finditer(line):
      ns = []
      print(mrs.start(), mrs.end())
      idx = mrs.start()
      # check if key exists
      if (i,idx+1) in nm: ns.append(nm[(i,idx+1)])
      if (i,idx-1) in nm: ns.append(nm[(i,idx-1)])
      if (i-1,idx) in nm: ns.append(nm[(i-1,idx)])
      if (i-1,idx+1) in nm: ns.append(nm[(i-1,idx+1)])
      if (i-1,idx-1) in nm: ns.append(nm[(i-1,idx-1)])
      if (i+1,idx) in nm: ns.append(nm[(i+1,idx)])
      if (i+1,idx+1) in nm: ns.append(nm[(i+1,idx+1)])
      if (i+1,idx-1) in nm: ns.append(nm[(i+1,idx-1)])
      #dedupe
      ns = list(set(ns))
      if len(ns) % 2 == 0 and len(ns) > 0:
        ret.append(int(ns[0])*int(ns[1]))
    i += 1
  print(ret)
  print(sum(ret))

if __name__ == "__main__":
  inp = process_input_file("test.txt")
  #part1(inp)
  part2(inp)
