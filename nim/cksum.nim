import strutils
import sequtils

proc diff(row: seq[int]): int =
  return (max(row) - min(row))

proc cksum(f: string): int =
  var sum = 0
  for line in lines f:
    sum += diff(map(line.split, parseInt))
  return sum

echo cksum("cksumin.txt")
