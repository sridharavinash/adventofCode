import itertools
import re
import collections

def process_input_file(filename):
  valid_re = re.compile("^\w+: (\d+)-(\d+) or (\d+)-(\d+)")
  valid_values = []
  nearby_tickets = []
  tickets = False
  line_no = 0
  line_off = 0
  invalid_line_nos = []
  for l in open(filename):
    line = l.strip()
    m = re.match(valid_re,line)
    if m:
      a,b,c,d = m.groups()
      vals = list(range(int(a),int(b)+1)) + list(range(int(c),int(d)+1))
      valid_values.append(vals)
    if line.startswith("nearby tickets"):
      tickets = True
      line_no += 1
      line_off = line_no
      continue
    if tickets:
      nearby_tickets.append([int(x) for x in line.split(',')])
    line_no += 1
  return itertools.chain(*valid_values), itertools.chain(*nearby_tickets), line_no, line_off

def part1(input):
  valid, tickets, total_lines, off = input
  valid_tickets = []
  valid = list(valid)
  invalid = []
  invalid_lines = []
  l = off
  i = 0
  for t in tickets:
    if t not in valid:
      invalid.append(t)
      invalid_lines.append(l)
    else:
      valid_tickets.append(t)
    if i % 20 == 0:
      l += 1
    i += 1
  print(sum(invalid))
  return invalid, invalid_lines

def process_input_file2(filename, invalid_line_nos):
  rexp = re.compile("^(\w+.*): (\d+)-(\d+) or (\d+)-(\d+)")
  valid_values = {}
  idx_guesses = collections.defaultdict(list)
  tickets = False
  your_ticket = False
  line_no = 1
  y_t = []
  for l in open(filename):
    if line_no in invalid_line_nos:
      line_no += 1
      continue
    line = l.strip()
    m = re.match(rexp,line)
    if m:
      label, a,b,c,d = m.groups()
      vals = list(range(int(a),int(b)+1)) + list(range(int(c),int(d)+1))
      valid_values[label] = vals
    if line.startswith("your ticket"):
      your_ticket = True
      line_no += 1
      continue
    if your_ticket:
      y_t = [int(zz) for zz in line.split(',')]
      line_no += 1
      your_ticket = False
      continue
    if line.startswith("nearby tickets"):
      tickets = True
      line_no += 1
      continue
    if tickets:
      idx = 0
      for f in line.split(','):
        field_val = int(f)
        for k in valid_values:
          if field_val not in valid_values[k]:
            idx_guesses[k].append(idx)
        idx += 1
    line_no += 1
  #print(idx_guesses)
  return idx_guesses,y_t

def part2(inputfile, invalid_line_nos):
  inp, y_t= process_input_file2(inputfile, invalid_line_nos)
  rng = set(range(20))
  diffs = collections.defaultdict(list)
  for i in inp:
    vals = sorted(set(inp[i]))
    possible_idxes = rng.difference(vals)
    diffs[len(possible_idxes)].append((i, possible_idxes))
  vals_taken = []
  final_mapping = {}
  prod = 1
  for j in range(1,20):
    if j not in diffs: 
      continue
    label = diffs[j][0][0]
    values = diffs[j][0][1]
    for v in values:
      if v not in vals_taken:
        vals_taken.append(v)
    value = vals_taken[-1]
    final_mapping[label] = value
    #print(final_mapping)
    if label.startswith('departure'):
      prod *= y_t[final_mapping[label]]
      #print(label, final_mapping[label], prod)
      
    
  print("final product:", prod)

if __name__ == "__main__":
  inp = process_input_file("input.txt")
  invalid_tickets, invalid_line_nos = part1(inp)
  #print(invalid_tickets)
  part2("input.txt", invalid_line_nos)
