import re
import datetime
import operator

def part1():
    s = {}
    d = {}
    timestamp_re = re.compile(r"^\[(.*)\]")
    event_re = re.compile(r"\] (.*)")
    guard_re = re.compile(r"Guard #(.\d*).*")
    for line in open("input.txt","r"):
        timestamp = re.match(timestamp_re,line)
        parsed_time = datetime.datetime.strptime(timestamp.group(1), "%Y-%m-%d %H:%M")
        event = re.search(event_re,line)
        d[parsed_time] = event.group(1)
    ordered =  {k: d[k] for k in sorted(d)}
    curr_guard = -1
    slept_hours_count = {}
    for k in ordered:
        guard_id = re.search(guard_re, ordered[k])
        if guard_id:
            curr_guard = int(guard_id.group(1))
            if curr_guard not in s:
                s[curr_guard] = 0
                slept_hours_count[curr_guard] = {'h':{}}
            slept = 0
        if "falls asleep" in ordered[k]:
            slept = k.minute
        if "wakes up" in ordered[k]:
            for i in range(slept,k.minute):
               if i in slept_hours_count[curr_guard]['h']:
                   slept_hours_count[curr_guard]['h'][i] += 1
               else:
                    slept_hours_count[curr_guard]['h'][i] = 1
            slept = k.minute - slept
            s[curr_guard] += slept
    mx = max(s.items(), key=operator.itemgetter(1))[0]
    mx_hour = max(slept_hours_count[mx]['h'].items(), key=operator.itemgetter(1))[0]
    slept = s[mx]
    total = mx * mx_hour
    print("final", mx,mx_hour,total)
    part2(slept_hours_count,mx,mx_hour)

def part2(s,mx,mx_hour):
    mm = mx_hour
    m_id = mx
    for guard in s:
        if s[guard]['h']:
            mx_hour = max(s[guard]['h'].items(), key=operator.itemgetter(1))[0]
            #print("comparing:",guard,mx_hour,s[guard]['h'][mx_hour])
            if s[guard]['h'][mx_hour] > s[m_id]['h'][mm]:
                mm = mx_hour
                m_id = guard
            #print(m_id,mm,s[m_id]['h'][mm])
    print("max minute slept:", mm, m_id, (mm * m_id))

if __name__ == "__main__":
    part1()