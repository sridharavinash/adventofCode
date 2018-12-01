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
            
def cksum(filename, fn):
    f = open(filename, 'r')
    cksum = 0
    cksum = [fn([int(x) for x in line.split()]) for line in f]
    return int(sum(cksum))

print(cksum("cksumin.txt", diff))
print(cksum("cksumin.txt", mod))
