import re

def part1():
    for line in open("input.txt","r"):
        print("final:",react(line))

def react(line):
    prev=''
    curr=''
    final = []
    for i in range(len(line)):
        curr = line[i]
        #print(prev,curr)
        if curr == prev:
            prev = curr 
            final.append(curr)
            continue
        if (curr == prev.upper()) or (curr == prev.lower()):
            if final:
                final.pop()
            if final:
                prev = final[-1]
            #print("final:", final, "count:",len(final))
            #input()
            continue
        prev = curr 
        final.append(curr)
    #print("final:", final, "count:",len(final), "initial:", len(line))
    return len(final)

def part2():
    for line in open("input.txt","r"):
        removed = {}
        for i in range(len(line)):
            rem = line[i].lower()
            rem_re = re.compile(rem, re.IGNORECASE)
            if rem not in removed:
                new_line = rem_re.sub('',line)
                removed[rem] = react(new_line)
        #print(removed)
        minn = min(removed, key=removed.get)
        print("min", minn, removed[minn])

if __name__ == "__main__":
    part1()
    part2()