import itertools
def part1():
  sums = []
  ns = []
  j=0
  k=0
  for l in open('input.txt'):
    line = l.strip()
    n = int(line)
    if k > 24:
      x = itertools.combinations(ns[j:k], 2)
      z = [i for i in x]
      s = [k+v for k,v in z]
      if n not in s:
        return n,ns
      j += 1

    ns.append(n)
    k+=1

def part2(n,ns):
  for i in range(len(ns)):
    z = itertools.accumulate(ns[i:])
    x = [zz for zz in z]
    if n in x:
      idx = x.index(n)
      #print(i, idx)
      s_slice = ns[i:i+idx+1]
      #print(s_slice)
      maxx = max(s_slice)
      minn = min(s_slice)
      return maxx+minn 

      
  pass 

if __name__ == "__main__":
    n,ns = part1()
    print(f"part1: {n}")
    print(f"part2: {part2(n,ns)}")