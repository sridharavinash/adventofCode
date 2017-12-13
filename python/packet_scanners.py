

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
    
def moves(s):
    print()
    total_moves = max(s.keys())
    state = {}
    d = {}
    pos = -1
    for l in s:
        state[l] = 0
        d[l] = 'd'
    #state,d = move_scanner(s,state,d)
    print(state,pos)
    sev = 0
    for i in range(total_moves+1):
        pos +=1
        print("before:",state, pos)
        if (pos in s) and (state[pos] == 0):
            sev += s[pos] * pos
            print("caught:", pos,"sev:",sev)
        state,d = move_scanner(s,state,d)
        print("after:",state, pos)
    return sev
        
        

scanner = {}
for line in open("../packets_test.in"):
    layer,depth = line.split(':')
    scanner[int(layer)] = int(depth)

print(scanner, max(scanner.keys()))
print(moves(scanner))
