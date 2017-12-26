def parse(f):
    lines = open(f)
    a = []
    for line in lines:
        i,o = line.strip().split('/')
        a.append((int(i),int(o)))
    return a


def findStarts(a,inn=0):
    return [i for i, x in enumerate(a) if x[0] == inn]

def findConnectors(rem,c):
    return [x for x in rem if ((x[0] == c or x[1] == c))]

maxx = 0
def findPaths(curr_node, remaining, curr_path=[]):
    global maxx
    #print("node:",curr_node)
    s = sum([x[0]+x[1] for x in curr_path])
    if s > maxx:
        maxx = s
        print("curr_path:", curr_path, len(curr_path),  s, "\nmaxx:", maxx)

    if curr_node == ():
        #print("curr_path", s, "maxx:", maxx)
        return curr_path

    if len(curr_path) == 0:
        c = curr_node[1]
    else:
        if curr_node[0] in curr_path[-1]: c =curr_node[1]
        else: c = curr_node[0]

    curr_path.append(curr_node)
    #print(curr_path,"||", remaining)
    #print("c:",c)
    conn = findConnectors([x for x in remaining if x != curr_node],c)
    #print("\t conn:", conn)
    for each in conn:
        curr_path = findPaths(each, [x for x in remaining if x != curr_node],curr_path)
        curr_path = curr_path[0:-1]

    return findPaths((), [x for x in remaining if x != curr_node],curr_path)
    
a = parse("../moat_p.in")
a = sorted(a)
startingPos = findStarts(a)

for i in startingPos:
    a_without_starts = [x for x in a if x != a[i]]
    findPaths(a[i],a_without_starts,[])
print ("Max:", maxx)



