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
inmat = np.pad(inmat,(384,384),'constant',constant_values=(0))
x,y = inmat.shape
cx= int(x/2)
cy = int(y/2)
directions = {
    'u':{'l': (0,-1,'l'), 'r':(0,1,'r')},
    'l':{'l':(1,0,'d'), 'r':(-1,0,'u')},
    'r':{'l':(-1,0,'u'),'r':(1,0,'d')},
    'd':{'l':(0,1,'r'),'r':(0,-1,'l')}
}

directions_noturn = {
    'u': (-1,0,'u'),
    'd': (1,0,'d'),
    'l': (0,-1,'l'),
    'r': (0,1,'r')
}

directions_reverse = {
    'u': (1,0,'d'),
    'd': (-1,0,'u'),
    'l': (0,1,'r'),
    'r': (0,-1,'l')
}


states = {'c':0,'w':2,'i':1,'f':3}
print()
curr = 'u'
infected = 0
for i in range(10000000):
    #print(inmat)
    #print(cx,cy)
    #input()
    if inmat[cx,cy] == states['i']:
        #infected , turn right, move forward
        #flag the node
        x,y,curr = directions[curr]['r']
        inmat[cx,cy] = states['f']
        cx += x
        cy += y
        continue
    if inmat[cx,cy] == states['c']:
        #weaken  node,turn left move forward
        x,y,curr = directions[curr]['l']
        inmat[cx,cy] = states['w']
        cx += x
        cy += y
        continue
    if inmat[cx,cy] == states['f']:
        #flagged, reverse
        x,y,curr = directions_reverse[curr]
        inmat[cx,cy] = states['c']
        cx += x
        cy += y
        continue
    if inmat[cx,cy] == states['w']:
        #weakened, no turn
        #infect the node
        x,y,curr = directions_noturn[curr]
        inmat[cx,cy] = states['i']
        infected += 1
        cx += x
        cy += y
        continue

print("infected:" , infected)
