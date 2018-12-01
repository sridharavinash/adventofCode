moves = {'d': (1,0), 'u': (-1,0), 'r':(0,1), 'l': (0,-1)}
opp_moves = {'d': 'u', 'l':'r', 'r':'l', 'u':'d'}

def calcnextDir(curr,r,c):
    for m in moves:
        if m == opp_moves[curr]:
            continue
        rx,cx = nextMov(m,r,c)
        try:
            if not route_lines[rx][cx].isspace():
                return m,rx,cx
        except IndexError:
            pass
    return  -1,-1,-1

def nextMov(curr,r,c):
    rn,cn = moves[curr]
    return r+rn,c+cn
    

route_lines = list(open("../tubes_p.in").readlines())

row = 1
col = route_lines[0].index('|')
next_c = ''
curr_direction = 'd'
path = []
count = 1
while row >0 and col >0:
    if next_c == '+':
        curr_direction,row,col =  calcnextDir(curr_direction,row,col)
        count += 1 # count on change of direction
        next_c = route_lines[row][col]
        if next_c.isupper(): path.append(next_c)
    row,col = nextMov(curr_direction, row, col)
    next_c = route_lines[row][col]
    if next_c.isupper(): path.append(next_c)
    count +=1
    if calcnextDir(curr_direction,row,col) == (-1,-1,-1): break

count += 1 #count at the end
print(''.join(path), count)


