import itertools

def part1():
  n = []
  grp = []
  for l in open("input.txt"):
    line = l.strip()
    if line == '':
      grp = list(itertools.chain.from_iterable(grp))
      n.append(len(set(grp)))
      grp = []
    grp.append([x for x in line])
  
  #print("end n:",n)
  return sum(n)  

def part2():
  n = []
  grp = []
  for l in open("input.txt"):
    line=l.strip()
    if line == '':
      #print(grp, len(grp))
      i = set(grp[0])
      for x in grp[1:]:
        i = i & set(x)
      #print("i:", i, len(i))
      n.append(len(i))
      grp = []

    if line != '': grp.append([x for x in line])
  
 

  #print("end n:",n)

  return sum(n)

if __name__ == "__main__":
    print("part1:",part1())
    print("part2:",part2())