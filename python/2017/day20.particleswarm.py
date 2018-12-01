import operator
from ast import literal_eval
import math
class Particle(object):
    def __init__(self,p,v,a):
        self.p = p
        self.v = v
        self.a = a
        self.receeding = False
        self.prev = math.inf

    def tick(self):
        self.v = tuple(map(operator.add,self.v, self.a))
        self.p = tuple(map(operator.add,self.p, self.v))

    def dist(self):
        d = sum([abs(x) for x in self.p])
        self.prev = d
        return abs(d)



def parse(line):
    ls = line.split(">,")
    p = ls[0].split("p=<")[1].strip()
    v = ls[1].split("v=<")[1].strip()
    a = ls[2].split("a=<")[1].replace('>','').strip()
    p = literal_eval(p)
    v = literal_eval(v)
    a = literal_eval(a)
    return p,v,a

particles = []
for line in open("../swarm_p2.in",'r'):
    p,v,a = parse(line)
    pt = Particle(p,v,a)
    particles.append(pt)

def part1():
    for i in range(10000):
        j = 0
        minn = math.inf
        min_p = 0
        for p in particles:
            p.tick()
            d = p.dist()
            if minn > d:
                min_p = j
                minn = d
            j+=1
        print(min_p)

def part2():
    particles_dict = {k:v for k,v in enumerate(particles)}
    for i in range(10000):
        part_pos = {}
        for j,p in particles_dict.items():
            p.tick()
            if p.p not in part_pos:
                part_pos[p.p] = [j]
            else:
                part_pos[p.p].append(j)

        for k,v in part_pos.items():
            if len(v) > 1:
                print(v,k)
                [particles_dict.pop(r) for r in v]
                
        print(len(particles_dict))

part2()

