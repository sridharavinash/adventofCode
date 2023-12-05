import itertools

def process_input_file(filename):
  for l in open(filename):
    line = l.strip()
    yield line

def part1(input):
  score = 0
  for line in input:
    cards = line.split("|")
    winning_cards = cards[0].split(':')[1].split()
    cards_dealt = cards[1].split()
    # find intersection
    set1 = set(winning_cards)
    set2 = set(cards_dealt)
    intsec = set1.intersection(set2)
    if len(intsec) == 0:
      continue
    # check if the lens match
    score += 2 ** (len(intsec)-1)
  print(score)

def part2(input):
  score = 0
  c = 1
  i = {}
  for line in input:
    if c in i:
      i[c] += 1
    else:
      i[c] = 1
    cards = line.split("|")
    winning_cards = cards[0].split(':')[1].split()
    cards_dealt = cards[1].split()
    # find intersection
    set1 = set(winning_cards)
    set2 = set(cards_dealt)
    intsec = set1.intersection(set2)
    for j in range(c+1, len(intsec)+c+1):
      if j in i:
         i[j] += 1 * i[c]
      else:
          i[j] = 1 * i[c]
    c += 1

  print(sum(i.values()))

if __name__ == "__main__":
  inp = process_input_file("input.txt")
  #part1(inp)
  part2(inp)
