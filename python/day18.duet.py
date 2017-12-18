import re
import queue


class Program(object):
    def __init__(self,infile):
        self.registers = {'end':False, 'jmp':0}
        self.q  = queue.Queue()
        self.infile = infile

    def mul (self,x,y):
        return x * y

    def snd(self,x):
        x_prev = x +'_prev'
        self.registers[x_prev] = self.registers[x]
        return self.registers[x]

    def rcv(self,x):
        prev = x + "_prev"
        if prev not in self.registers:
            return
        if self.registers[x] > 0:
            self.registers["end"] = True
            print("rcv:",self.registers[prev])

    def jgz(self,reg,jmp):
        if reg.isdigit():
            if int(reg) > 0: return jmp
        if self.registers[reg] > 0:
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
        if ins == "add":
            if reg not in self.registers:
                self.registers[reg] = 0
            self.registers[reg] += val
        if ins == "mul":
            if reg not in self.registers:
                self.registers[reg] = 0
            self.registers[reg] *= val
        if ins == "mod":
            self.registers[reg] %= val
        if ins == "snd":
            self.snd(reg)
        if ins == "rcv":
            self.rcv(reg)
        if ins == "jgz":
           self.registers['jmp'] =  self.jgz(reg,val)

    def run(self):
        lines = open(self.infile).readlines()
        i = 0
        while not self.registers["end"]:
            r = self.parse(lines[i])
            self.process(r)
            if abs(self.registers['jmp']) > 0:
                i += (self.registers['jmp'])
                self.registers['jmp'] = 0
            else:
                i+=1

p = Program("../duet_p.in")
p.run()

