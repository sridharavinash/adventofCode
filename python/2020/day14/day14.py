import itertools
import re

def process_input_file(filename):
  rexp = re.compile("mask = (.*)|mem\[(\d+)\] = (\d+)")
  for l in open(filename):
    line = l.strip()
    line_s = [c.strip() for c in line.split('=')]
    yield rexp.match(line).groups()

def part1(input):
  mask = b''
  mask_dict={}
  reg = {}
  for m,addr,val in input:
    if m:
      mask_dict={}
      mask = [x for x in m]
      i = 0
      for b in mask:
        if b != 'X':
          mask_dict[i] = b
        i += 1
    else:
      v = int(val)
      a = int(addr)
      lb = f'0{len(mask)}b'
      bin_v = list(format(v,lb))
      for k in mask_dict:
        bin_v[k] = mask_dict[k]
      bin_v = ''.join(bin_v)
      reg[a] = int(bin_v,2)
  print(sum(reg.values()))
  
def part2(input):
  mask = b''
  mask_dict = {}
  reg = {}
  for m,addr, val in input:
    if m:
      mask = [x for x in m]
    else:
      a = int(addr)
      lb = f'0{len(mask)}b'
      bin_a = list(format(a, lb))
      v = int(val)
      masked_possible = list(map(lambda x,y: y if y == 'X' or y == '1' else x, bin_a, mask))
      possible_addrs_count = masked_possible.count('X')
      possible_values = list(itertools.product(*["01"] * possible_addrs_count))
      subsituted_str = ''.join(map(lambda c: '%s' if c == 'X' else c, masked_possible))
      all_addresses = [int(format(subsituted_str%z),2) for z in possible_values]
      #print(possible_addrs_count)
      for addr in all_addresses:
        reg[addr] = v 
  #print(reg)
  print(sum(reg.values()))

if __name__ == "__main__":
  inp = process_input_file("input.txt")
  #part1(inp)
  part2(inp)
