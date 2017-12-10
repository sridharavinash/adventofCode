#!/usr/local/bin/python3

def subseq(seq,pos,ll):
    """ returns the wrapped elements of the list"""
    #print("pos:",pos, "ll:",ll, "seq:",seq)
    listlen = len(seq)
    start = pos
    sub=[]
    for i in range(ll):
        while pos >= listlen:
            pos = listlen - pos
        sub.append(seq[pos])  
        pos += 1
    return sub
    
def knothash(seq, lengths,pos=0,skip=0):
    ll = len(seq)
    for l in lengths:
        sub = subseq(seq,pos,l)
        sub.reverse()
        j = pos
        # copy over the reversed array to the orig array
        for i in sub:
            while j >= ll:
                j = ll - j
            seq[j] = i
            j+=1
        #print("after reverse:", seq, "l+skip:", l+skip)
        pos += l + skip
        #print("pos before adj:", pos)
        while pos > ll:
            pos = pos - ll
        skip +=1
    #print("new position:",pos, "skip",skip)
    #print("final:",pos,skip,seq,seq[0]*seq[1])
    return seq,pos,skip

def test():
    s = [i for i in range(256)]
    assert "3efbe78a8d82f29979031a4aa0b16a9d" == part2(s,"1,2,3")
    s = [i for i in range(256)]
    assert "63960835bcdc130f0b66d7ff4f6a5a8e" == part2(s,"1,2,4")
    s = [i for i in range(256)]
    assert "33efeb34ea91902bb2f59c9920caa6cd" == part2(s,"AoC 2017")
    s = [i for i in range(256)]
    part2(s,"157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30")

    
def part2(seq,inp):
    std = [17,31,73,47,23]
    inp_list = [ord(y) for y in ''.join([x for x in inp])]
    inp_list = inp_list + std
    seqi = seq
    posi = 0
    skipi = 0
    ll  = len(seqi)

    #64 rounds of the hashes to get the sparse hash
    for i in range(64):
        seqi,posi,skipi = knothash(seqi,inp_list,posi,skipi)
        while posi > ll:
            posi = posi - ll

    xored = []
    start = 0
    end = 16
    
    #generate the dense hash
    for i in range(16):
        sub = seqi[start:end]
        x = 0
        for j in sub:
            x ^= j
        xored.append(x)
        start += 16
        end += 16

    #represent this as a hex string
    hexed = ''.join([hex(x).replace('0x','').zfill(2) for x in xored])
    print(inp,"=>", hexed)
    return hexed
    
def puzzle_input():
    s = [i for i in range(256)]
    print(knothash(s,[157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30]))

def part1():
    s = [0,1,2,3,4]
    print(knothash(s,[3,4,1,5]))
          
test()
#puzzle_input()
#part1()
