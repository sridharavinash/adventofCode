import numpy
import itertools
import networkx as nx
import matplotlib.pyplot as plt
import collections

def part1():
  ratings = []
  for l in open("test.txt"):
    line = l.strip()
    ratings.append(int(line))
  ratings.append(max(ratings) + 3)
  diffs = numpy.diff(sorted(ratings))
  print(sorted(ratings),diffs)
  _, counts = numpy.unique(diffs, return_counts=True)
  print(counts)
  return ((counts[0]+1)  * counts[1])

def count_iter_items(iterable):
    counter = itertools.count()
    collections.deque(zip(iterable, counter), maxlen=0)
    return next(counter)

def part2():
  ratings = []
  for l in open("test.txt"):
    line = l.strip()
    ratings.append(int(line))
  ratings.append(max(ratings) + 3)
  ratings.append(0)
  ratings = sorted(ratings)
  g = nx.DiGraph()
  for i in ratings:
    g.add_node(i)
  
  for i in range(len(ratings)):
    k = ratings[i]
    a,b,c = k+1, k+2, k+3
    x = filter(lambda y: y in ratings, [a,b,c])
    for j in x:
      g.add_edge(k,j)
  #print(g.nodes(), g.edges())
  # print("computing paths...")
  # sp = nx.all_simple_paths(g,0, max(ratings))
  # print("summing")
  # print(sum(1 for _ in sp))

    
    
    
  #print(count_iter_items(sp))
  #print(sp.edges())
  #print(len(tuple(sp)))
 
  nx.draw(g, with_labels = True)
  plt.show()


def part21():
  ratings = []
  for l in open("input.txt"):
    line = l.strip()
    ratings.append(int(line))
  ratings.append(0)
  ratings = sorted(ratings)
  # paths[n] is the total paths from 0 to n
  paths = collections.defaultdict(int)
  paths[0] = 1
  maxx = max(ratings)
  for adapter in ratings:
      for diff in range(1, 4):
          next_adapter = adapter + diff
          if next_adapter in ratings:
              paths[next_adapter] += paths[adapter]
  print(paths[maxx])


if __name__ == "__main__":
    #print(f"part1: {part1()}")
  
  p2 = part21()