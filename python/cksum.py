#!/usr/local/bin/python3

def diff(row):
    return abs(max(row) - min(row))

def cksum(filename):
    f = open(filename, 'r')
    cksum = 0
    cksum = [diff([int(x) for x in line.split()]) for line in f]
    return sum(cksum)

print(cksum("cksumin.txt"))
