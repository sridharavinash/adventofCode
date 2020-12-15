import re
import itertools
import collections

def part1():
  dir = {
    'E':{'R90': 'S' , 'L90': 'N', 'R180': 'W', 'R270': 'N', 'L180': 'W', 'L270': 'S'},
    'W':{'R90': 'N' , 'L90': 'S', 'R180': 'E', 'R270': 'S', 'L180': 'E', 'L270': 'N'},
    'N':{'R90': 'E' , 'L90': 'W', 'R180': 'S', 'R270': 'W', 'L180': 'S', 'L270': 'E'},
    'S':{'R90': 'W' , 'L90': 'E', 'R180': 'N', 'R270': 'E', 'L180': 'N', 'L270': 'W'}
  }
  rxp = re.compile("^([ESNWLRF])(\d+)$")
  curr_pos = [0]
  curr_dir = 'E'
  hist = {'E': 0, 'N':0 , 'S': 0 , 'W':0}
  for l in open('input.txt'):
    line = l.strip()
    m = rxp.match(line)
    d = m.groups()[0]
    pos = int(m.groups()[1])
    if d == 'F':
      hist[curr_dir] += pos
    elif d in ['N', 'W','S', 'E']:
      hist[d] += pos 
    elif d in ['R', 'L']:
      turn = f'{d}{pos}'
      curr_dir = dir[curr_dir][turn]

    #print(d,pos, hist,curr_dir)
  m_d = abs(hist['E'] - hist['W']) + abs(hist['N'] - hist['S'])
  print(f'm_d : {m_d}')

def part2():
  dir = {
    'E':{'R90': 'S' , 'L90': 'N', 'R180': 'W', 'R270': 'N', 'L180': 'W', 'L270': 'S'},
    'W':{'R90': 'N' , 'L90': 'S', 'R180': 'E', 'R270': 'S', 'L180': 'E', 'L270': 'N'},
    'N':{'R90': 'E' , 'L90': 'W', 'R180': 'S', 'R270': 'W', 'L180': 'S', 'L270': 'E'},
    'S':{'R90': 'W' , 'L90': 'E', 'R180': 'N', 'R270': 'E', 'L180': 'N', 'L270': 'W'}
  }
  rxp = re.compile("^([ESNWLRF])(\d+)$")
  curr_pos = [0]
  curr_dir = ['E','N']
  hist = {'E': 0, 'N':0 , 'S': 0 , 'W':0}
  wp = {'E': 10, 'N':1 , 'S': 0 , 'W':0}
  for l in open('input.txt'):
    line = l.strip()
    m = rxp.match(line)
    d = m.groups()[0]
    pos = int(m.groups()[1])
    if d == 'F':
      for k in wp:
        hist[k] += (pos * wp[k]) 
    elif d in ['N', 'W','S', 'E']:
      wp[d] += pos
    elif d in ['R', 'L']:
      temp = {}
      turn = f'{d}{pos}'
      for k in wp:
        turn_k = dir[k][turn]
        temp[turn_k] = wp[k]
      wp = temp

    #print(d,pos, hist,curr_dir)
  m_d = abs(hist['E'] - hist['W']) + abs(hist['N'] - hist['S'])
  print(f'm_d : {m_d}')  

if __name__ == "__main__":
    #part1()
    part2()