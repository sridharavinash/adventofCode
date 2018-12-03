def part1():
    sq = {}
    sq_ids = {}
    maxx=0
    maxy=0
    overlapped=[]
    ids=[]
    for line in open("input.txt","r"):
        i,_,xy,size = line.split()
        x,y = xy.replace(":","").split(',')
        sizex,sizey = size.split('x')
        occx,occy = [int(x),(int(x)+int(sizex))], [int(y),(int(y)+int(sizey))]
        if  occx[1]> maxx:
            maxx = occx[1]
        if occy[1] > maxy:
            maxy = occy[1]
        #print(i,x,y,sizex,sizey, occx,occy,maxx,maxy)
        ids.append(i)
        for kx in range(occx[0],occx[1]):
            for ky in range(occy[0],occy[1]):
                if (kx,ky) in sq:
                    sq[kx,ky] = 'X'
                    sq_ids[kx,ky].append(i)
                    overlapped.extend(sq_ids[kx,ky])
                else:
                    sq[kx,ky] = '.'
                    sq_ids[kx,ky] = [i]
    #print(maxx,maxy)
    #print(sq_ids)
    #print(overlapped)
    a = 0
    for k in sq:
        if sq[k] == 'X':
            a +=1

    print("Total:", a)
    print("not overlapped id:",set(ids).difference(set(overlapped)))

if __name__ == "__main__":
    part1()