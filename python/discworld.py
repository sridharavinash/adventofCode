#!/usr/local/bin/python3

class Tree(object):
    def __init__(self,name, weight,children=None,parent=None):
        self.name = name
        self.weight = weight
        self.children = children

    def total_weight(self):
        s = self.weight
        for c in self.children:
            s += c.total_weight()
        return s

    def __str__(self):
        return self.name
    
def parseLine(line):
    l = line.split()
    n = l[0]
    w = int(l[1].replace('(','').replace(')',''))
    c = [x.replace(',','') for x in l[3:]]
    return n,w,c

def traverseTree(node):
    global ns
    s = {}
    bal = 0
    for c in node.children:
        tw = c.total_weight()
        if tw in s:
            s[tw]['count'] += 1
            s[tw]['nodes'].append(c)
            bal = tw
        else:
            s[tw] = {'count':0 , 'nodes':[c]}
            s[tw]['count'] = 1
    for k,v in s.items():
        if v['count'] == 1:
            n = v['nodes'][0]
            rebal = bal-k
            print("off_balance:",n,k,bal,"node:",n.weight,"off_bal:", bal-k)
            if rebal < 0:
                ns = ((n.name, n.weight - abs(rebal)))
            else:
                 ns = ((n.name, n.weight + rebal))     
            s = traverseTree(n)
    return ns

def main(filename):
    nodes = {}
    parents = {}
    #parse tree to tree obj
    for line in open(filename):
        n,w,c = parseLine(line)
        tree = Tree(n,w,c)
        if len(c) == 0:
            nodes[n]=tree
        else:
            parents[n]=tree

    #generate tree pruning children and orphans
    seen = []
    for p in parents:
        c =[]
        for child in parents[p].children:
            if child in nodes:
                c.append(nodes[child])
            else:
                seen.append(child)
                c.append(parents[child])
        parents[p].children = c
    for p in seen:
        parents.pop(p)
    root = parents.popitem()[1]
    print("root:", root.name)
    print(traverseTree(root))


    
main("disc_test.in")
ns = (0,0)
main("disc.in")
