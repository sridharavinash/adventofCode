import itertools
import re

def process_input_file(filename):
  for l in open(filename):
    line = l.strip()
    yield line

def part1(input):
  stack = []
  s = []
  add = lambda x,y: x+y
  mul = lambda x,y: x*y
  ops = []
  for line in input:
    for l in line:
      if l.strip() == '':
        continue
      if l == '+':
        # add the two numbers
        ops.append(add)
        continue
      elif l == '*':
        #multiply numbers
        ops.append(mul)
        continue
      elif l == '(':
        ops.append('(')
        continue
      elif l == ')':
        o = ops.pop()
        n = [stack.pop()]
        n_op = [o]
        while n_op[-1] != '(':
          n.append(stack.pop())
          n_op.append(ops.pop())
        n_op.reverse()
        for o in n_op:
          if o == '(': continue
          a = n.pop()
          b = n.pop()
          c_val = o(a,b)
          n.append(c_val)
        stack.append(n.pop())
      else:
        stack.append(int(l))
    stack.reverse()
    for o in ops:
      a = stack.pop()
      b = stack.pop()
      stack.append(o(a,b))
    ops = []
    #print(stack)
    s.append(stack.pop())
  print(sum(s))

def part2(input):
  stack = []
  s = 0
  add = lambda x,y: x+y
  mul = lambda x,y: x*y
  ops = []
  for line in input:
    for l in line:
      if l.strip() == '':
        continue
      if l == '+':
        # add the two numbers
        ops.append(add)
        continue
      elif l == '*':
        #multiply numbers
        ops.append(mul)
        continue
      elif l == '(':
        ops.append('(')
        continue
      elif l == ')':
        o = ops.pop()
        n = [stack.pop()]
        n_op = [o]
        while n_op[-1] != '(':
          n.append(stack.pop())
          if len(n_op)>0 and n_op[-1] == add:
            c_val = n.pop() + n.pop()
            n.append(c_val)
            n_op.pop()
          n_op.append(ops.pop())
        while len(n_op) > 0:
          o = n_op.pop()
          if o == '(': continue
          a = n.pop()
          b = n.pop()
          c_val = o(a,b)
          n.append(c_val)
        stack.append(n.pop())
        if len(ops)>0 and ops[-1] == add:
          c_val = stack.pop() + stack.pop()
          stack.append(c_val)
          ops.pop()        
      else:
        stack.append(int(l))
        if len(ops)>0 and ops[-1] == add:
          c_val = stack.pop() + stack.pop()
          stack.append(c_val)
          ops.pop()
    while len(ops) > 0:
      o = ops.pop()
      a = stack.pop()
      b = stack.pop()
      stack.append(o(a,b))
    a = stack.pop()
    print(a)
    s+=a
  print(s)

if __name__ == "__main__":
  #inp = process_input_file("input.txt")
  #part1(inp)
  inp = process_input_file("input.txt")
  part2(inp)