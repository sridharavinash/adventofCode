import itertools
import collections

n_coords = list(itertools.filterfalse(lambda x: x == (0,0,0), itertools.product(range(-1,2), repeat=3)))
n_coords4 = list(itertools.filterfalse(lambda x: x == (0,0,0,0), itertools.product(range(-1,2), repeat=4)))

lenn = 10
def process_input_file(filename):
  for l in open(filename):
    line = l.strip()
    row_state = map(lambda x:True if x == '#' else False, line)
    yield row_state

def get_neighbors(c):
  x,y,z = c
  for vx,vy,vz in n_coords:
    yield (vx + x, vy +y, vz +z)

def get_neighbors4(c):
  x,y,z,w = c
  for vx,vy,vz,vw in n_coords4:
    yield (vx + x, vy +y, vz +z, vw + w)

def part1(input):
  activated= []
  i = 0
  j = 0
  z = 0
  for row in input:
    r = list(row)
    for state in r:
      if state:
        activated.append((i,j,z))
      j+= 1
    j = 0
    i+= 1
  
  for i in range(6):
    current_activated = []
    for z in range(-2-i,i+2):
      for x in range(-lenn-i,i+lenn):
        for y in range(-lenn-i,i+lenn):
          #print(x,y,z)
          neighbors = list(get_neighbors((x,y,z)))
          active_neighbors = [x for x in neighbors if x in activated]
          if len(active_neighbors) == 3:
            current_activated.append((x,y,z))
          if (x,y,z) in activated and (len(active_neighbors) == 2):
            current_activated.append((x,y,z))
    activated = current_activated
    print(len(set(activated)))

def part2(input):
  activated= []
  i = 0
  j = 0
  z = 0
  w = 0
  for row in input:
    r = list(row)
    for state in r:
      if state:
        activated.append((i,j,z,w))
      j+= 1
    j = 0
    i+= 1
  
  for i in range(6):
    current_activated = []
    for w in range(-2-i, i+2):
      for z in range(-2-i,i+2):
        for x in range(-lenn-i,i+lenn):
          for y in range(-lenn-i,i+lenn):
            #print(x,y,z)
            neighbors = list(get_neighbors4((x,y,z,w)))
            active_neighbors = [x for x in neighbors if x in activated]
            if len(active_neighbors) == 3:
              current_activated.append((x,y,z,w))
            if (x,y,z,w) in activated and (len(active_neighbors) == 2):
              current_activated.append((x,y,z,w))
    activated = current_activated
    print(len(set(activated)))

if __name__ == "__main__":
  inp = process_input_file("input.txt")
  #part1(inp)
  part2(inp)