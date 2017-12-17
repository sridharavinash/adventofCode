step = 1
step = 343
buff = [0]
pos = 0
val = 0
s = 0
part2 = 50000000
while val < 2017:
    for i in range(step):
        pos += 1
        if pos >= len(buff):
            pos = len(buff) - pos
    val += 1
    buff.insert(pos+1, val)
    if pos == 0:
        s += buff[1]
        print(buff[1],s)

    pos = pos+1
    
#print(buff[buff.index(2017)+1])
print(buff[1])
print("---")
val = 1
s = step -1
x = 1

while val < 50000000:
    val = int((((step+1)*val)+s-1)/step)
    s = (s + val) % (step+1)
    if ( s % step == 0):
        print(val,s)

