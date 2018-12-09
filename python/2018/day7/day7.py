import re

started=[]
can_start=[]
workers = {}
for i in range(0,2):
    workers[i] = {'curr':'.', 'steps_remaining':0}
ticks = {}
for i,c in zip(range(1,27),list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
    ticks[c]=i

def part1():
    global can_start
    global started
    events = {}
    line_re = re.compile("^Step (.*) must be finished before step (.*) can begin.")
    for line in open("input.txt","r"):
        parsed_line = re.match(line_re,line)
        step = parsed_line.group(1)
        before = parsed_line.group(2)
        if step not in events:
            events[step] = [before]
        else:
            events[step].append(before)
        events[step] = sorted(events[step])
        print(f"{step} -> {before}")
    print(events)
    print()
    for k in events:
        traverse(k,events)

def traverse(s,events):
    global can_start
    global started
    global workers
    for k in events:
        if k in started: continue
        if can_it_start(k,events,started):
            if k not in can_start:
                can_start.append(k)
    can_start = sorted(can_start)
    print("can_start", can_start)
    if len(can_start) < 1:
        return
    started.append(can_start[0])
    ss = can_start[0]
    can_start.remove(can_start[0])
    print(''.join(started))
    print(can_start)
    traverse(ss,events)
    
    

def can_it_start(k,dic,started):
    if k not in dic:
        return False
    for i in dic:
        if i in started:
            continue
        if k in dic[i]:
            return False
    return True

if __name__ == "__main__":
    part1()