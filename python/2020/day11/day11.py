import itertools
import copy

def part1():
  arr = []
  for l in open('test.txt'):
    line = l.strip()
    arr.append(line)

  for r in arr: print(r)
  print('------------')
  brr=[]
  ibrr = []
  for r in arr:
    brr.append(['#' if c == 'L' else c for c in r])
    ibrr.append(['#' if c == 'L' else c for c in r])

  for r in brr: print(r)
  i =0
  j =0
  
  occupied=[]
  prev_occ=[]
  ii = 1
  while True:
    if i >= len(brr):
      print('end of iteration', ii)
      ii+=1
      i=0
      j=0
      brr = copy.deepcopy(ibrr)
      if set(prev_occ) == set(occupied):
        print(f"stable: occupied:{len(occupied)}")
        break
      prev_occ = copy.deepcopy(occupied)
      occupied=[]
      #for yy in brr:
      #  print(yy)

    idxes = [(i-1,j),(i+1,j),(i,j+1),(i,j-1),(i+1, j+1),(i-1,j-1), (i-1, j+1), (i+1, j-1) ]
    #filter edges
    idxes = itertools.filterfalse(lambda x: x[0] < 0 or x[1] <0, idxes)
    #filter ends
    idxes = list(itertools.filterfalse(lambda x: x[0] >= len(brr) or x[1] >= len(brr[i]), idxes))
    occ = 0
    if j >= len(brr[i]):
      #next row
      j = 0
      i+=1
      #print()
      continue

    # skip floor
    if brr[i][j] == '.': idxes=[]
    
    # check adjacent elements
    for x,y in idxes:
      if brr[x][y] == '#':
         occ += 1
    
    if occ > 3:
      # flip empty/occupied
      c = 'L'
    elif occ == 0 and brr[i][j] == 'L':
      c = '#'
    else:
      c = brr[i][j]
    ibrr[i][j] = c
    if c == '#':
      occupied.append((i,j))
    #print(c,end='')
    #next element
    j+=1

def part2():
  arr = []
  for l in open('input.txt'):
    line = l.strip()
    arr.append(line)

  for r in arr: print(r)
  print('------------')
  brr=[]
  ibrr = []
  for r in arr:
    brr.append(['#' if c == 'L' else c for c in r])
    ibrr.append(['#' if c == 'L' else c for c in r])

  for r in brr: print(r)
  i =0
  j =0
  
  occupied=[]
  prev_occ=[]
  iterations = 1
  while True:
    if i >= len(brr):
      print('end of iteration', iterations)
      iterations+=1
      i=0
      j=0
      brr = copy.deepcopy(ibrr)
      if set(prev_occ) == set(occupied):
        print(f"stable: occupied:{len(occupied)}")
        break
      prev_occ = copy.deepcopy(occupied)
      occupied=[]
      #for yy in brr:
      #  print(yy)
    
    pos = {
    'top' : [i-1, j],
    'down' : [i+1,j],
    'right' : [i, j+1] ,
    'left' :  [i, j-1],
    'topleft' : [i-1,j-1],
    'topright' : [i-1,j+1],
    'downleft' : [i+1,j-1],
    'downright' : [i+1, j+1]      
    }
    m_cols = len(brr[0]) -1
    m_rows = len(brr) -1
    occ = 0
    if j > m_cols:
      #next row
      j = 0
      i+=1
      print()
      continue

    if brr[i][j] == '.': 
      j+=1
      print('.',end='')
      continue

    for p in pos:
      x,y = pos[p]
      if x <0 or y <0 or y > m_cols or x > m_rows:
        continue
      cont = False
      if brr[x][y] == '.':
        if p == 'top': x -= 1
        elif p == 'down': x += 1
        elif p == 'right': y += 1
        elif p == 'left' : y -= 1
        elif p == 'topleft': x -= 1; y -= 1
        elif p == 'topright': x-=1;y+=1
        elif p == 'downleft': x+=1;y-=1
        elif p == 'downright':x += 1; y += 1
        if x <0 or y <0 or y > m_cols or x > m_rows:
            continue
        cont = False
        while brr[x][y] == '.':
          if p == 'top': x -= 1
          elif p == 'down': x += 1
          elif p == 'right': y += 1
          elif p == 'left' : y -= 1
          elif p == 'topleft': x -= 1; y -= 1
          elif p == 'topright': x-=1;y+=1
          elif p == 'downleft': x+=1;y-=1
          elif p == 'downright':x += 1; y += 1
          if x <0 or y <0 or y > m_cols or x > m_rows:
            cont = True
            break
      if cont: continue
      if brr[x][y] == '#':
        occ += 1

    #skip floor 
    if brr[i][j] == '.': occ = 0

    if occ > 4:
      # flip empty/occupied
      c = 'L'
    elif occ == 0 and brr[i][j] == 'L':
      c = '#'
    else:
      c = brr[i][j]
    ibrr[i][j] = c
    if c == '#':
      occupied.append((i,j))
    print(c,end='')
    #next element
    j+=1

if __name__ == "__main__":
    #part1()
    part2()

