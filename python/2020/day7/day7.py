import re
rexp = re.compile("^(.*) bags contain (.*).$")
rexp2 = re.compile("^(\d+|no) (.*) bag|bags")

def path_find(k, deps): 
  if k == '':
    return False
  if 'shiny gold' in deps[k] :
    return True
  for each in deps[k]:
    if path_find(each, deps):
      return True
  return False

def part1():
  deps = {}
  shiny = []
  for l in open("input.txt"):
    line = l.strip()
    m = re.match(rexp, line).groups()
    main_bag = m[0]
    container_bags = m[1].split(',')
    for i in container_bags:
      cm = re.match(rexp2, i.strip())
      if cm:
        c_bag = cm.groups()[1]
        if c_bag == 'other':
          c_bag = ''
        if main_bag in deps: 
          deps[main_bag].append(c_bag)
        else:
          deps[main_bag] = [c_bag]

  for k in deps:
    if k == 'shiny gold': continue
    if path_find(k, deps):
      shiny.append(k)
  return(len(set(shiny)))


def part2():
  deps = {}
  shiny = []
  for l in open("input.txt"):
    line = l.strip()
    m = re.match(rexp, line).groups()
    main_bag = m[0]
    container_bags = m[1].split(',')
    for i in container_bags:
      cm = re.match(rexp2, i.strip())
      if cm:
        c_bag = cm.groups()[1]
        c_bag_count = cm.groups()[0]
        if c_bag == 'other':
          c_bag = 'none'
          c_bag_count = '0'
        c_bag_count = int(c_bag_count)
        if main_bag in deps: 
          deps[main_bag].append((c_bag, c_bag_count))
        else:
          deps[main_bag] = [(c_bag, c_bag_count)]
  return count_recursive('shiny gold', deps, 0)

def count_recursive(k, deps, acc):
  if k == 'none' or len(deps[k]) == 0:
    return 0
  #print(k, deps[k])
  acc = sum([x[1] for x in deps[k]])
  for each in deps[k]:
    acc += each[1] * count_recursive(each[0], deps, acc)
  #print(acc)
  return acc
  
if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
