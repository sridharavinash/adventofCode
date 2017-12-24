import re
import pdb

class Program(object):
    def __init__(self,infile,debug_mode=0):
        self.registers = {'jmp':0, 'a':0, 'b': 0, 'c': 0 , 'd': 10, 'e': 0, 'f': 0, 'g':0, 'h':0, 'x':0}
        if debug_mode:
            self.registers['a'] = 1

        self.infile = infile
        self.count = 0


    def jnz(self,reg,jmp):
        if reg.isdigit():
            if int(reg) != 0: return jmp
        if self.registers[reg] != 0:
            return jmp
        return 0

    def parse(self,line):
        r = re.match(r"^(?P<ins>\w+) (?P<reg>\w+) ?(?P<val>.*)",line)
        return r

    def parse_val(self,v):
        if v in self.registers:
            return int(self.registers[v])
        else:
            try:
                return int(v, 10)
            except ValueError:
                return 0

    def process(self,r):
        ins = r.group('ins')
        reg = r.group('reg')
        v = r.group('val')
        val = self.parse_val(v)
        if ins == "set":
            self.registers[reg] = val
        if ins == "sub":
            self.registers[reg] -= val
        if ins == "mul":
            self.count+=1
            self.registers[reg] *= val
        if ins == "jnz":
           self.registers['jmp'] =  self.jnz(reg,val)
    def run(self):
        lines = open(self.infile).readlines()
        i = 0
        print(i,lines[i])
        print(self.registers)
        while 1:
            #print(i,lines[i])
            self.registers['x'] = self.registers['d'] * self.registers['e']
            if i == 15:
                print("setting f to 0")
                print(self.registers)
                pdb.set_trace()
            if i == 20 or i == 26:
                print(i,lines[i])
                print(self.registers)
                pdb.set_trace()
                #self.registers['e'] = self.registers['b']
                #self.registers['d'] = self.registers['b']
                
            r = self.parse(lines[i])
            self.process(r)
            if abs(self.registers['jmp']) > 0:
                i += (self.registers['jmp'])
                self.registers['jmp'] = 0
            else:
                i+=1
            if i >= len(lines): break

p = Program('../coproc_p.in', debug_mode=1)
p.run()
print(p.registers)


def part2():
    b = 109900
    c = 126900
    ct = 0
    h = 0
    while b <= c:
        ct = 0
        for i in range(2,b,1):
            if b % i == 0:
                ct += 1
        if ct > 0: h+=1
        print("count:",ct,"b:",b,"h:",h)
        b+=17
