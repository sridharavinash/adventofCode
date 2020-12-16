import itertools

def part1():
  i = 0
  ts = 0
  buses = []
  for l in open("input.txt"):
    if i == 0:
      ts = int(l)
    else:  
     buses = list(itertools.filterfalse(lambda x: x == 'x', l.split(',')))
     buses = [int(x) for x in buses]
    i+=1
  minn = ts
  min_d  = 0
  for t in buses:
    d = int(ts/t)
    for i in range(d, d + 2):
      m = abs(ts - (t *i))
      #print(t, t*i , m)
      if m < minn and t*i > ts:
        minn = m
        min_d = t
        #print('min',minn, min_d)

  #print(minn, min_d)
  print(minn * min_d)

def part2():
  #inp = '7,13,x,x,59,x,31,19'
  #inp = '17,x,13,19'
  inp = '19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,599,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,x,x,x,x,23,x,x,x,x,x,x,x,761,x,x,x,x,x,x,x,x,x,41,x,x,13'
  #inp = '67,x,7,59,61'
  #inp = '1789,37,47,1889'
  #inp = '2,3,x,5'
  bus = {}
  j = 0
  first = 0
  n = 1
  for i in inp.split(','):
    if i == 'x' :
      j+=1
      continue
    bus[int(i)] = j
    n *= int(i)
    if j == 0: first = int(i)
    j +=1
  print(bus)
  ff=[]
  x = 0
  step = 1

  for b in bus:
    while (x + bus[b]) % b:
      x += step
    step *= b
  
  print(f'{x}')
  

if __name__ == "__main__":
    #part1()
    part2()

