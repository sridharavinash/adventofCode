import numpy as np

def convertToMat(row):
    return [1 if x =='#' else 0 for x in row.strip()]

def convertToPatternRow(row):
    return ''.join(['#' if x == 1 else '.' for x in row])


def convertToPattern(mat):
    ml = mat.tolist()
    pattern=''
    for m in ml:
       pattern += convertToPatternRow(m)
       pattern += '/'
    #remove trailing
    return pattern[:-1]
    
def parsePattern(pat):
    rows = pat.split('/')
    n = []
    for r in rows:
        c = convertToMat(r)
        n.append(c)
    return np.matrix(n)

def splitMat(mat,n):
    mats= []
    x,y = mat.shape
    c = 0
    for c in range(0,y,n):
        for r in range(0,x,n):
            m = mat[r:r+n,c:c+n]
            mats.append(m)
    return mats

def start(inmat,n,pat_dict):
    for i in range(n):
        print(inmat.shape)
        if inmat.shape[0] % 2 == 0:
            mats = splitMat(inmat,2)
        else:
            mats = splitMat(inmat,3)
        inmat = matchPattern(mats,pat_dict,inmat.shape)
    print("non_zero:",np.count_nonzero(inmat))

def matchPattern(mats,pats,pshape):
    x,y = mats[0].shape
    if pshape[0] % 2 == 0: factor = 2
    else: factor = 3

    l = len(mats)
    if l > 1:
        nx = int(pshape[0]/factor) * (x + 1)
        ny = int(pshape[0]/factor) * (y + 1)
    else:
        nx = x + 1
        ny = y + 1
    matches= np.zeros((nx,ny))
    r=0
    c=0
    q = 0
    for m in mats:
        for i in range(4):
            rot90 = np.rot90(m,i)
            rot90_flip = np.flip(rot90,1)
            rot90_c = convertToPattern(rot90)
            rot90_flip_c = convertToPattern(rot90_flip)
            #print(i,"looking for:",rot90_c)
            #print(i,"flipped:",rot90_flip_c)
            if rot90_c in pats:
                #print(i,"matched:", pats[rot90_c])
                fillmat = parsePattern(pats[rot90_c])
                x1,y1 = fillmat.shape
                matches[r:r+x1,c:c+y1] = fillmat
                break
            if rot90_flip_c in pats:
                #print(i,"matched(flipped):", pats[rot90_flip_c])
                fillmat = parsePattern(pats[rot90_flip_c])
                x1,y1 = fillmat.shape
                matches[r:r+x1,c:c+y1] = fillmat
                break
        q+=1
        r+=(x+1)
        if r >= nx:
            r = 0
            c+=(y+1)
        
    return matches


inp = np.matrix('0 1 0; 0 0 1; 1 1 1')
pat_dict = {}
for line in open('../fractal_p.in'):
    in_pat, out_pat = line.split('=>')
    pat_dict[in_pat.strip()] = out_pat.strip()

#print("patterns:", pat_dict)
start(inp,18,pat_dict)

