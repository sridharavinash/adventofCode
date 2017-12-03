#!/usr/local/bin/python3

#for part 1
def diff(row):
    return abs(max(row) - min(row))

#for part 2
def mod(row):
    for i in row:
        for j in row:
            if i == j:
                continue
            if i % j == 0:
                return i/j
            
def cksum(filename):
    f = open(filename, 'r')
    cksum = 0
    cksum = [mod([int(x) for x in line.split()]) for line in f]
    return sum(cksum)

print(cksum("cksumin.txt"))
