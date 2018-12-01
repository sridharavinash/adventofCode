import knothash 
from skimage.measure import label
import numpy as np

def repbin(c):
    return bin(int(c,16)).replace('0b','').zfill(4)

def repHash(l):
    print( ''.join(['#' if x == '1' else '.' for x in l]))

def repHash2(l):
    print( [str(x) if x > 0 else '.' for x in l])

#inp = 'flqrgnkx'
inp = 'nbysizxe'
z = 0
regions = 0
r = np.empty((128,128),dtype=int)
for i in range(128):
    suffix= '-' + str(i)
    h = knothash.khash(inp+suffix)
    b = ''.join([repbin(x) for x in h])
    z += sum(x == '1' for x in b)
    x = [ 1 if x == '1' else 0 for x in b]
    r[i] = x
_,regions= label(r,connectivity=1,neighbors=4,return_num=True)
print("Total Used:", z, "regions:",regions)
