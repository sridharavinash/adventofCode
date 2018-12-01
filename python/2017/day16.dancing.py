
def spin(l,pos):
    return l[-pos:] + l[:-pos]

def swap_pos(l,a,b):
    t = l[a]
    l[a] = l[b]
    l[b] = t
    return l

def partner(l,a,b):
    ai = l.index(a)
    bi = l.index(b)
    l[ai] = b
    l[bi] = a
    return l


def main():
    progs = list("abcdefghijklmnop")
    seq = open("../dance.in").read()
    seen = []
    for i in range(10**9):
        pj = ''.join(progs)
        if pj in seen:
            print('seen:',pj,i, (10**9 % i))
            print("final:",seen[10**9 % i])
            return
        seen.append(pj)
        print(i,pj)
        for step in seq.split(','):
            s = step[0]
            if s == 's':
                pos = step[1:]
                progs = spin(progs,int(pos))
            if s == 'x':
                a,b = step[1:].split("/")
                progs = swap_pos(progs,int(a),int(b))
            if s == 'p':
                a,b = step[1:].split("/")
                progs = partner(progs,a,b)

    print()
    print("final:",''.join(progs))

main()
