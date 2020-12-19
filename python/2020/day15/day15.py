import collections
import copy


def part1(input):
  spoken_turns = collections.defaultdict(list)
  turn = 1
  stop = 30000001
  for i in input:
    spoken_turns[i] = [turn]
    turn += 1
  spoken = copy.deepcopy(input)

  while True:
    last_spoken = spoken[-1]
    spoken_turns_of_last_spoken = spoken_turns[last_spoken][-1]
    times_spoken_of_last_spoken = len(spoken_turns[last_spoken])
    if turn == stop:
      break
    if times_spoken_of_last_spoken == 1:
      spoken.append(0)
      spoken_turns[0].append(turn)
    else:
      n = spoken_turns_of_last_spoken - spoken_turns[last_spoken][-2]
      spoken.append(n)
      spoken_turns[n].append(turn)
    turn += 1
    print('\r', stop-turn,end='')
  print()
  print(f"{stop}th spoken:", spoken[-1])

if __name__ == "__main__":
  part1([0,3,6])
  #part1([2,0,1,7,4,14,18])
  #part2(inp)
