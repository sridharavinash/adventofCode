import numpy as np

def parsePattern(filename):
    n = []
    for r in open(filename):
        c = convertToMatRow(r)
        n.append(c)
    return np.matrix(n)

def convertToMatRow(row):
    return [1 if x =='#' else 0 for x in row.strip()]

def convertToPatternRow(row):
    print(row[:])
    return ['#' if x == 1 else '.' for x in row]

inmat = parsePattern("../spvirus_p.in")
inmat = np.pad(inmat,(192,192),'constant',constant_values=(0))
x,y = inmat.shape
cx= int(x/2)
cy = int(y/2)
directions = {
    'u':{'l': (0,-1,'l'), 'r':(0,1,'r')},
    'l':{'l':(1,0,'d'), 'r':(-1,0,'u')},
    'r':{'l':(-1,0,'u'),'r':(1,0,'d')},
    'd':{'l':(0,1,'r'),'r':(0,-1,'l')}
}
print()
curr = 'u'
infected = 0
for i in range(10000):
    #print(inmat)
    print("infected:" , infected)
    #print(cx,cy)
    #input()
    if inmat[cx,cy] == 1:
        #infected , turn right, move forward
        #clean the node
        x,y,curr = directions[curr]['r']
        inmat[cx,cy] = 0
        cx += x
        cy += y

    else:
        #clean node,turn left move forward
        #infect the node
        x,y,curr = directions[curr]['l']
        infected += 1
        inmat[cx,cy] = 1
        cx += x
        cy += y

    
