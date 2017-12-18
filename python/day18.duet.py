import re
import queue
import threading

class Program(object):
    def __init__(self,infile,p=0):
        self.id = p
        self.registers = {'jmp':0, 'p': p}
        self.q  = queue.Queue()
        self.infile = infile
        self.otherp = None
        self.count = 0
        self.waiting = False

    def setOtherP(self,otherp):
        self.otherp = otherp

    def mul (self,x,y):
        return x * y

    def snd(self,x):
        v = self.parse_val(x)
        print("sending item", v, self.id,self.registers)
        if self.id == 1:
            self.count += 1
            print("count:",self.count)
        self.otherp.q.put(v)

    def rcv(self,x):
        print("wating on rcv", self.id)
        self.waiting = True
        if self.otherp.waiting:
            print(self.count)
        item = self.q.get()
        print("got item", item, self.id,self.registers)
        self.waiting = False
        if item :
            self.registers[x] = item

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
        while 1:
            r = self.parse(lines[i])
            self.process(r)
            if abs(self.registers['jmp']) > 0:
                i += (self.registers['jmp'])
                self.registers['jmp'] = 0
            else:
                i+=1

p0 = Program("../duet_p.in",p=0)
p1 = Program("../duet_p.in",p=1)
p0.setOtherP(p1)
p1.setOtherP(p0)
t0 = threading.Thread(target = p0.run)
t0.start()

t1 = threading.Thread(target = p1.run)
t1.start()

for t in [t0,t1]:
    t.join()
