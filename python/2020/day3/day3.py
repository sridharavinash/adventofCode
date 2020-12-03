def part1(p,skip=1):
  trees = 0
  pos = p
  c = 0
  for l in open("input.txt"):
    line = l.strip()
    c += 1
    if c == 1:
      continue
    if skip>1 and c % skip == 0:
      continue
    if pos >= (len(line)):
        pos = pos - (len(line) )
    #print(f"{line[pos]} || pos:{pos} || line:{c} ||{line}")
    if line[pos] == '#':
      trees += 1
    pos += p
  return trees

def part2():
  total_mul = 1
  for pos in [1,3,5,7]:
    t = part1(pos)
    print(f'part2: right:{pos} down:1 - {t}')
    total_mul *= t
  
  jump_2 = part1(1,2)
  print(f'part2: right:1, down:2 - {jump_2}')
  return total_mul * jump_2

if __name__ == "__main__":
  print(f"part 1 trees: {part1(3)}")
  print()
  print("total product:", part2())