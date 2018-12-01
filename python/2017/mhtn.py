#!/usr/local/bin/python3

import math

def nearestSq(num):
    n = int(math.sqrt(num))
    if n*n == num:
        return num,(n-1)*(n-1),n
    return (n+1)*(n+1),(n*n),n+1

def dist(num):
    sq,psq,n = nearestSq(num)
    top = (n-1,n-1)
    o = int(int(n-1)/2)
    orig = (o,o)
    i = sq
    j = 0
    k = n
    p ={}
    print(sq,psq,n,top,orig)
    while i > psq:
        while j < n:
            p[i] = (j,n-1)
            i-=1
            j+=1
        j-=1
        while j > 0:
            p[i] = (n-1,j-1)
            i -=1
            j -=1
    d = abs(p[num][0] - orig[0]) + abs(p[num][1]-orig[1])
    print(p[num])
    return num, d

print(dist(361527))

