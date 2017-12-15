import knothash

def repbin(c):
    return bin(int(c,16)).replace('0b','').zfill(4)

def countAdj(l,prev, prevm):
    s = 0
    inr=False
    r = [0]*len(l)
    m  = max(prev)
    print(m, prevm)
    for i in range(len(l)):
        if l[i] == "1" and not inr:
            inr = True
            if prev[i] == 0:
                s = m +1
                m = s
            else:
                s = prev[i]
        if l[i] == "0":
            inr = False
            r[i] = 0

        if inr:
            if prev[i] != 0:
                r[i] = prev[i]
                j = i-1
                while r[j] != 0 and j >=0:
                    r[j] = prev[i]
                    j -= 1
                j = i+1
                s = prev[i]
                if prevm < max(r):
                    m = max(r)
                else:
                    m = prevm
            else:
                r[i] = s
        #repHash2(r)
    repHash2(r)
    return r, max(r)

def repHash(l):
    print( ''.join(['#' if x == '1' else '.' for x in l]))

def repHash2(l):
    print( [str(x) if x > 0 else '.' for x in l])
    
inp = 'flqrgnkx'
inp = 'nbysizxe'
z = 0
xx = [0]*128
m=0
pm = m
regions = 0
for i in range(128):
    suffix= '-' + str(i)
    h = knothash.khash(inp+suffix)
    b = ''.join([repbin(x) for x in h])
    z += sum(x == '1' for x in b)
    xx,m = countAdj(b,xx,pm)
    if m > pm:
        pm = m
print(pm)
            
print("Total Used:", z, "regions:",regions)
