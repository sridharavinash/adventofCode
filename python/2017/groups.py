#!/usr/bin/local/python3

def detectGroup(stream,g,garbage,inception_level,gc=0):

    if len(stream) == 0: return g,gc
    if stream[0] == "<" and not(garbage):  garbage = True
    if stream[0] == ">":
        gc -= 1
        garbage = False
    if stream[0] == "}" and (not garbage):
        g += inception_level
        inception_level -= 1
    if stream[0] == "{" and (not garbage): inception_level +=1
    if garbage == True: gc += 1

    if stream[0] == "!":
        gc -= 1
        return detectGroup(stream[2:],g,garbage,inception_level,gc)

    return detectGroup(stream[1:],g,garbage,inception_level,gc)

def main(s):
    print("*********")
    groups = detectGroup(s,0,False,0)
    print(groups)
    print()
    return groups

def part1():
    assert 1 == main("{}")
    assert 6 == main("{{{}}}")
    assert 5 == main("{{},{}}")
    assert 16 == main("{{{},{},{{}}}}")
    assert 1 == main("{<a>,<a>,<a>,<a>}")
    assert 9 == main("{{<ab>},{<ab>},{<ab>},{<ab>}}")
    assert 9 == main("{{<!!>},{<!!>},{<!!>},{<!!>}}")
    assert 3 == main("{{<a!>},{<a!>},{<a!>},{<ab>}}")
    

def part2():
    assert (1,17) == main("{<random characters>}")
    assert (1,3) == main("{<<<<>}")
    assert (1,2) == main("{<{!>}>}")
    assert (1,0) == main("{<!!>}")
    assert (1,0) == main("{<!!!>>}")
    assert (1,10) == main('{<{o"i!a,<{i<a>}')

def puzzle_input():
    with open("../groups.in",'r') as in_file:
        ss = in_file.read()
        main(ss)

part2()
puzzle_input()
