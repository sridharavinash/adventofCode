#!/usr/bin/local/python3

def detectGroup(stream):
    s = 0
    l = 0
    gbg = False
    ig = False
    gc = 0
    for i in stream:
        if i == "!" and not ig:
            ig = True
            continue
        if ig:
            ig = False
            continue
        if gbg :
            gc += 1
        if i == "<":
            gbg = True
            continue
        if i == ">":
            gc -= 1
            gbg = False
        if i == "{" and not gbg: l += 1
        if i == "}" and not gbg:
            s += + l
            l -= 1
    return s,gc
        

def main(s):
    print("*********")
    score,gc = detectGroup(s)
    print(score,gc)
    print()
    return score,gc


def part1():
    assert 1 == main("{}")[0]
    assert 6 == main("{{{}}}")[0]
    assert 5 == main("{{},{}}")[0]
    assert 16 == main("{{{},{},{{}}}}")[0]
    assert 1 == main("{<a>,<a>,<a>,<a>}")[0]
    assert 9 == main("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0]
    assert 9 == main("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0]
    assert 3 == main("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0]
    

def part2():
    assert 17 == main("{<random characters>}")[1]
    assert 3 == main("{<<<<>}")[1]
    assert 2 == main("{<{!>}>}")[1]
    assert 0 == main("{<!!>}")[1]
    assert 0 == main("{<!!!>>}")[1]
    assert 10 == main('{<{o"i!a,<{i<a>}')[1]

def puzzle_input():
    with open("../groups.in",'r') as in_file:
        ss = in_file.read()
        main(ss)
part1()
part2()
puzzle_input()
