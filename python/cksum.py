#!/usr/local/bin/python3

def diff(row):
    return abs(max(row) - min(row))

def cksum(filename):
    f = open(filename, 'r')
    cksum = 0
    for line in f:
        cksum += diff([int(x) for x in line.split
