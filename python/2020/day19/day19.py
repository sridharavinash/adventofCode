import itertools
import re


def process_input_file(filename):
  rules = {}
  checks = []
  for l in open(filename):
    if l == '\n' or len(checks)>0:
      checks.append(l.strip())
      continue
    line = l.strip()
    line = line.split(':')
    if line[1].strip() == '"a"':
      rules[int(line[0])] = 'a'
      continue
    if line[1].strip() == '"b"':
      rules[int(line[0])] = 'b'
      continue

    rules[int(line[0])] = line[1].strip().split()
    
  return rules,checks[1:]


def traverse_rules(start,r, acc):
  if r[start] == 'a' or r[start] == 'b':
    #print(r[start],end='')
    return r[start]
  for v in r[start]:
    if v == '|':
      acc += '|'
      continue
    acc += traverse_rules(int(v),r, '')
  return '(' + acc + ')'

def part1(input):
  r,checks = input
  regex = traverse_rules(0, r, '')
  regex = f'^{regex[1:-1]}$'
  # print()
  # print(f'regex: {regex}')
  matches = 0
  for c in checks:
    if re.match(regex, c):
      matches+=1
  print(f"Total Matches: {matches}")

def part2(input):
  r,checks = input
  # replace as per puzzle
  #r[8] = ['42', '|', '42', '8']
  #r[11] = ['42', '31', '|', '42', '11', '31']
  r42 = traverse_rules(42,r,'')
  r31 = traverse_rules(31,r,'')

  # print(r42)
  # print(r31)
  # print(r8)
  # print(r11)

  max_len_checks = max(len(x) for x in checks)
  #print('final_regex:', regex)
  newr8 = f'{r42}+'
  matches = 0
  for i in range(1,max_len_checks):
    newr11 = f"({r42}){{{i}}}{r31}{{{i}}}"
    regex = f'^{newr8}{newr11}$'
    for c in checks:
      if re.match(regex, c):
        #print(c)
        matches+=1
  print(f"Total Matches: {matches}")

if __name__ == "__main__":
  inp = process_input_file("test2.txt")
  #part1(inp)
  part2(inp)
  inp = process_input_file("input.txt")
  part2(inp)
