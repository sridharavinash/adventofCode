
proc calc(in_list: string): int =
  var sum: int = 0
  var step: int = (len(in_list)/2).int32
  for i in countup(0, len(in_list)-1):
    var curr = in_list[i]
    var nextd: char
    if (i+step) > (len(in_list))-1:
      var idx = (i+step) - (len(in_list))
      nextd = in_list[idx]
    else:
      nextd = in_list[i+step]
  
    if curr == nextd:
      sum += int(curr) - int('0')
  return sum

assert 6 == calc("1212")
assert 0 == calc("1221")
assert 4 == calc("123425")
assert 12 == calc("123123")
assert 4 == calc("12131415")
