graph = {}

def build_graph(node,edges):
    global graph
    if node not in graph:
        graph[node] = edges

def traverseGraph(start,p=[]):
    global graph
    p.append(start)
    for e in graph[start]:
        if e in p:
            continue
        traverseGraph(e,p)
    return p
        
for line in open("../dp_p.in"):
    a,bl = line.split("<->")
    a = int(a)
    bl = [int(x) for x in bl.strip().split(',')]
    build_graph(a,bl)

    
#print(graph)
seen = []
groups = 0
for n in graph:
    ps = []
    if n not in seen:
        ps = traverseGraph(n,ps)
        seen += ps
        groups += 1
        print(len(ps))
print(groups)
