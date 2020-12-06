def part1():
  ids = []
  for l in open("input.txt"):
    line = l.strip()
    #print(line[:7])
    r = ''.join(['0' if c == 'F' else '1' for c in line[:7]])
    c = ''.join(['0' if x == 'L' else '1' for x in line[7:]])
    r_d = int(r,2)
    c_d = int(c,2)
    ids.append(((r_d*8)+c_d))
  
  return max(ids), ids

def part2():
  _, ids = part1()
  ids = sorted(ids)
  rr = list(range(min(ids), max(ids)+1))
  return set(rr).difference(set(ids))

if __name__ == "__main__":
    print("part1:",part1()[0])
    print("part2:",part2())