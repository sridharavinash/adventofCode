import operator

def part1():
    ords = []
    for line in open("input.txt","r"):
        x,y = line.split(',')
        intx = int(x)
        inty = int(y)
        ords.append((intx,inty))
    gridx,gridy = max(ords)
    mxc = max([gridx,gridy])    
    print("grid:",gridx, gridy, mxc)
    min_d = {}
    count={}
    corners=[]
    for ix in range(0,mxc+1):
        for iy in range(0,mxc+1):
            ds=[]
            for cx,cy in ords:
                d = abs(cx-ix) + abs(cy-iy)
                ds.append(d)
            minn=min(ds)
            idx = ds.index(minn)
            dups=[i for i, x in enumerate(ds) if x == minn]

            if len(dups) > 1:
                min_d[(ix,iy)]=-1
            else:
                min_d[(ix,iy)] =ords[idx]
                if ix in [0,mxc+1] or iy in [0,mxc+1]:
                    corners.append(ords[idx])
                if ords[idx] in count:
                    count[ords[idx]] +=1
                else:
                    count[ords[idx]] = 1
    #print(set(corners))
    for k in set(corners):
        count.pop(k)
    print(count)
    mx = max(count.items(), key=operator.itemgetter(1))
    print("Max Area:", mx)

def part2():
    limit=10000
    ords = []
    for line in open("input.txt","r"):
        x,y = line.split(',')
        intx = int(x)
        inty = int(y)
        ords.append((intx,inty))
    gridx,gridy = max(ords)
    mxc = max([gridx,gridy]) 
    print(mxc)
    rc = 0
    for ix in range(0,mxc+2):
        for iy in range(0,mxc+2):
            sumd=0
            for cx,cy in ords:
                d = abs(cx-ix) + abs(cy-iy)
                #print(f"({cx}-{ix})+({cy}-{iy}) = {d}")
                sumd+=d
                #print((ix,iy),(cx,cy),d)
            if sumd < limit:
                rc+=1
    print("total:",rc)


if __name__ == "__main__":
    #part1()
    part2()