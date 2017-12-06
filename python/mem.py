#!/usr/local/bin/python3

def mem_redist(in_mem):
    redistributions = 0
    all_dist = []
    llen = len(in_mem)
    curr_redist = ""
    while True:
        maxx = max(in_mem)
        max_index = in_mem.index(maxx)
        in_mem[max_index] = 0
        idx = max_index + 1
        done = False
        for i in range(maxx):
            if idx >= llen: idx = llen - idx
            in_mem[idx] += 1
            idx += 1
        redistributions += 1
        curr_redist = ''.join(str(x) for x in in_mem)
        if curr_redist in all_dist:
            return redistributions, (redistributions - all_dist.index(curr_redist) -1 )
        all_dist.append(curr_redist)

            
print( mem_redist([0,2,7,0]))
print(mem_redist([4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3]))


