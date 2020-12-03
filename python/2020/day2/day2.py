def extract(line):
  split_lines = line.split()
  minn = int(split_lines[0].split('-')[0])
  maxn = int(split_lines[0].split('-')[1])
  char = split_lines[1].split(':')[0]
  passwd = split_lines[2]
  return minn,maxn,char,passwd

def part1():
  total = 0
  for line in open("input.txt"):
    minn, maxn, char, passwd = extract(line)
    count = passwd.count(char)
    if count >= minn and count <= maxn:
      total += 1
  return total

def part2():
  total = 0
  for line in open("input.txt"):
    minn, maxn, char, passwd = extract(line)
    pos1 = minn - 1 
    pos2 = maxn - 1
    if (passwd[pos1] == char and passwd[pos2] != char) or (passwd[pos1] != char and passwd[pos2] == char):
      total += 1
  return total
  

if __name__ == "__main__":
  print(part1())
  print(part2())