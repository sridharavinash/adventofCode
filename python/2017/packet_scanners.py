
def move_scanner(s,state,d):
    for i in s:
        if d[i] == 'u':
            state[i] -= 1
        else:
            state[i] += 1
        if ((state[i] + 1) == s[i]):
            d[i] = 'u'
        else:
            if ((state[i] - 1) < 0):
                d[i] = 'd'
    return state,d

def Caught(s,delay):
    for i in s:
        depth = s[i]
        whenZero = (2*(depth-1))
        if (i+delay) % whenZero == 0:
            #print("caught:",i)
            return True
    print("delay:",delay)
    return False  
    
def moves(s,delay=0):
    total_moves = max(s.keys())
    state = {}
    d = {}
    pos = -1
    for l in s:
        state[l] = 0
        d[l] = 'd'
    for x in range(delay):
        state,d = move_scanner(s,state,d)
    print("delay:",delay,state)
    sev = 0
    caught = False
    for i in range(total_moves+1):
        pos +=1
        #print("before:",state, pos)
        if (pos in s) and (state[pos] == 0):
            sev += s[pos] * pos
            print("caught:", pos,"sev:",sev)
            caught = True
            #return sev, caught
            #print("caught:",state, pos)
        state,d = move_scanner(s,state,d)
    return sev,caught
                

scanner = {}
for line in open("../packets_p.in"):
    layer,depth = line.split(':')
    scanner[int(layer)] = int(depth)

print(scanner, max(scanner.keys()))
#print(moves(scanner,2))
c = True
delay = 0
while c:
    c = Caught(scanner,delay)
    delay +=1

