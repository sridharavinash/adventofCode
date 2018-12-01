#!/usr/local/bin/python3

registers = {}
highest_val = 0
def shouldModify(expr):
    reg = expr[1]
    op = expr[2]
    val = int(expr[3])
    if op == "<":
        return registers[reg] < val
    if op == ">":
        return registers[reg] > val
    if op == "<=":
        return registers[reg] <= val
    if op == ">=":
        return registers[reg] >= val
    if op == "!=":
        return registers[reg] != val
    if op == "==":
        return registers[reg] == val

def modify(reg,op,delta,expr):
    global highest_val
    global registers
    if shouldModify(expr):
        if op ==  "inc":
            registers[reg] += delta
        else:
            registers[reg] -= delta
        if registers[reg] > highest_val:
            highest_val = registers[reg]
            

def parseLine(line):
    global registers
    s = line.split()
    if s[0] not in registers:
        registers[s[0]] = 0
    if s[4] not in registers:
        registers[s[4]] = 0
    return s[0], s[1], int(s[2]), s[3:]

for line in open("registers.in"):
    r_to_modify,op,delta,expr = parseLine(line)
    modify(r_to_modify,op,delta,expr)

print(registers)
print("max:", max(registers.values()))
print("highest_val:", highest_val)
