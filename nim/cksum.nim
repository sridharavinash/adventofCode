import strutils
import sequtils

#for part 1
proc diff(row: seq[int]): int =
  return (max(row) - min(row))

#for part2
proc modd(row: seq[int]): int =
  for i,v1 in row:
    for j,v2 in row:
      if v1 == v2:
        continue
      if v1 mod v2 == 0:
        return int(v1/v2)
  

proc cksum(f: string): int =
  var sum = 0
  for line in lines f:
    sum += modd(map(line.split, parseInt))
  return sum

echo cksum("cksumin.txt")
