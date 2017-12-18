import re


registers = {'end':False, 'jmp':0}

def mul (x,y):
    return x * y

def snd(x):
    x_prev = x +'_prev'
    registers[x_prev] = registers[x]
    return registers[x]

def rcv(x):
    prev = x + "_prev"
    if prev not in registers:
        return
    if registers[x] > 0:
        registers["end"] = True
        print("rcv:",registers[prev])

def jgz(reg,jmp):
    if reg.isdigit():
        if int(reg) > 0: return jmp
    if registers[reg] > 0:
        return jmp
    return 0

def parse(line):
    r = re.match(r"^(?P<ins>\w+) (?P<reg>\w+) ?(?P<val>.*)",line)
    return r

def parse_val(v):
    if v in registers:
        return int(registers[v])
    else:
        try:
            return int(v, 10)
        except ValueError:
            return 0

def process(r):
    ins = r.group('ins')
    reg = r.group('reg')
    v = r.group('val')
    val = parse_val(v)
    if ins == "set":
        registers[reg] = val
    if ins == "add":
        if reg not in registers:
            registers[reg] = 0
        registers[reg] += val
    if ins == "mul":
        if reg not in registers:
            registers[reg] = 0
        registers[reg] *= val
    if ins == "mod":
        registers[reg] %= val
    if ins == "snd":
        snd(reg)
    if ins == "rcv":
        rcv(reg)
    if ins == "jgz":
       registers['jmp'] =  jgz(reg,val)
    
lines = open("../duet_p.in").readlines()
i = 0
while not registers["end"]:
    r = parse(lines[i])
    process(r)
    if abs(registers['jmp']) > 0:
        i += (registers['jmp'])
        registers['jmp'] = 0
    else:
        i+=1
    
