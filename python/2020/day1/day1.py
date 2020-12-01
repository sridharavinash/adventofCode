def part1(summ):
  diffs = {}
  for line in open("input.txt"):
    n = int(line)
    diffs[n]  = abs(n - summ)
  found = False
  vals = []
  for k in diffs:
    v = diffs[k]
    if v in diffs:
      vals = [v,k, v*k]
      found = True
      break
  return diffs, vals, found

def part2():
  diffs,_, _ = part1(2020)
  for k in diffs:
   _, vals, found = part1(diffs[k])
   if found and (k + vals[0] + vals[1]) == 2020:
     return [k, vals[0], vals[1], k*vals[2]]

if __name__ == "__main__":
  _, vals, f = part1(2020)
  if f:
    print("part1:", vals)
  print("part2:", part2())