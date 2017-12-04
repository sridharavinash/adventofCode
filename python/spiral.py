#!/usr/local/bin/python3

def right(x,y):
    return x+1,y
def up(x,y):
    return x,y+1
def left(x,y):
    return x-1,y
def down(x,y):
    return x,y-1
def bright(x,y):
    return  x-1, y+1
def bleft(x,y):
    return x+1,y-1
def tright(x,y):
    return x+1,y+1
def tleft(x,y):
    return x-1,y-1

pos = [right,left,down,up,tright,tleft,bright,bleft]

def getMx(x,y):
    try:
        return mx[(x,y)]
    except KeyError:
        mx[(x,y)] = 0
        return 0
    
def getAdjCVals(x,y):
    s=0
    for p in pos:
        a,b = p(x,y)
        s+= getMx(a,b)
    mx[(x,y)]=s
    printMx()
    return s

mx = {}

def points(num):
    x = y = 0
    n=1
    mx[(x,y)] = n
    step = 1
    while step <= num:
        if step % 2 == 0 :
            x,y= right(x,y)
            n=getAdjCVals(x,y)
            for i in range(step):
                x,y=up(x,y)
                n=getAdjCVals(x,y)
            for i in range(step):
                x,y=left(x,y)  
                n=getAdjCVals(x,y)
        else:
            x,y=left(x,y)
            n=getAdjCVals(x,y)
            for i in range(step):
                x,y=down(x,y)
                n=getAdjCVals(x,y)
            for i in range(step):
                x,y=right(x,y)
                n=getAdjCVals(x,y)
        step+=1
        print("step:",step)

def printMx():
    for x in range(-6,6):
        print("\n")
        for y in range(6,-6,-1):
            print(getMx(y,x),end='\t')
    print("\n")
    
points(7)
