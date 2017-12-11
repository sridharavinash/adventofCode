#!/usr/local/bin/python3

d_calc = {
    "ne": (1,0,-1),
    "se": (1,-1,0),
    "s": (0,-1,1),
    "sw": (-1,0,1),
    "nw": (-1,1,0),
    "n": (0,1,-1)
}

def nextTile(direction,cords):
    d = d_calc[direction]
    return (d[0]+cords[0],d[1] + cords[1], d[2] + cords[2])
    
def distcalc(orig,curr):
    return max(curr[0]-orig[0],curr[1],orig[1],curr[2]-orig[2])
    
def traverse(path):
    psplit = path.split(',')
    orig = (0,0,0)
    curr = (0,0,0)
    max_d = 0
    for p in psplit:
        curr = nextTile(p,curr)
        dd = distcalc(orig,curr)
        if max_d < abs(dd):
            max_d = abs(dd)

    print("final:",curr,"distance:",dd,"max:",max_d)
    return dd

def puzzle_input():
    path = open("../hextile.in","r").read()
    traverse(path)
    
assert 3 == traverse("ne,ne,ne")
assert 0 == traverse("ne,ne,sw,sw")
assert 2 == traverse("ne,ne,s,s")
assert 3 == traverse("se,sw,se,sw,sw")
puzzle_input()
