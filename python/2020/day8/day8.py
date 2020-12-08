def part1(lines):
  line_no = 0
  acc = 0
  processed = []
  terminated = False
  while True:
    if line_no >= len(lines):
      terminated = True
      print("line:", line_no)
      break
    
    line = lines[line_no]
    if line_no in processed:
      break
    processed.append(line_no)
    s = line.split()
    cmd = s[0]
    val = int(s[1])
    if cmd == 'nop':
      line_no += 1
      continue
    if cmd == 'acc':
      acc += val
      line_no += 1
    if cmd == 'jmp':
      line_no += val
  return acc,terminated


def part2():
  jmps = []
  nops = []
  lines = []
  n = 0
  for l in open("input.txt"):
    line = l.strip()
    s = line.split()
    cmd = s[0]
    val = int(s[1])
    if cmd == 'jmp':
      jmps.append(n)
    if cmd == 'nop':
      nops.append(n)
    n += 1
  
  for i in jmps:
    lines = [l.strip() for l in open("input.txt")]
    lines[i] = 'nop 0'
    acc, terminated = part1(lines)
    if terminated:
      print(f" jmp -> nop {i}: acc: {part1(lines)}")
      return acc


  return len(jmps),len(nops)

if __name__ == "__main__":
    lines = [l.strip() for l in open("input.txt")]
    #print(f"part1: {part1(lines)}")
    print(f"part2: {part2()}")