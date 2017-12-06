import strutils
import sequtils

proc isPhraseValid(p: string): bool =
  var wp: seq[string] = @[]
  for v in p.split:
    if v in wp:
      return false
    wp.add(v)
  return true

assert true == isPhraseValid("aa bb cc dd ee")
assert false == isPhraseValid("aa bb cc dd aa")
assert true ==  isPhraseValid("aa bb cc dd aaa")
  
