import itertools

def process_input_file(filename):
  for l in open(filename):
    line = l.strip()
    yield line

def part1(input):
  n = ""
  for line in input:
    for c in line:
      if c.isnumeric():
        n += c
        break
    # reverse the line
    rev = line[::-1]
    for c in rev:
      if c.isnumeric():
        n += c
        break
    n+= ","
  # strip the last comma
  n = n[:-1]
  # split the string into a list
  n = n.split(",")
  # convert the list into a list of integers
  n = [int(i) for i in n]
  # sum the list
  print(n, sum(n))

def part2(input):
  n = ""
  digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  digitmap = {"zero": "0","one": "1" , "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "1": "1" , "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0"}
  for line in input:
    firstn = ""
    firstc = ""
    firstd= ""
    i = -1
    j = len(line)
    #find first digit
    for c in line:
      if c.isnumeric():
        firstn = c 
        i = line.index(c)
        break  
    #find first word number
    for d in digits:
      if d in line:
        if line.index(d) < j:
          firstc = d
          j = line.index(d)
    if i < j:
      firstd = firstn 
    else: firstd = firstc
    if i == -1: firstd = firstc
    n += digitmap[firstd]
    firstd = ""
    firstn = ""
    firstc = ""
    i = -1
    j = -1
    #find second digit
    rev = line[::-1]
    for c in rev:
      if c.isnumeric():
        firstn = c 
        i = line.rindex(c)
        break
    #find second word number
    for d in digits:
      if d in line:
        if line.rindex(d) > j:
          firstc = d
          j = line.rindex(d)
    if i > j: 
      firstd = firstn
    else: firstd = firstc
    if i == -1: firstd = firstc
    if j == -1: firstd = firstn
    n += digitmap[firstd]
    #print the last values of the list
    print(line, n[-2], n[-1])
    n+= ","
    
  # strip the last comma
  n = n[:-1]
  # split the string into a list
  n = n.split(",")
  # convert the list into a list of integers
  n = [int(i) for i in n]
  # sum the list
  print(n, sum(n))

      
      
  

if __name__ == "__main__":
  inp = process_input_file("input.txt")
  #part1(inp)
  part2(inp)
