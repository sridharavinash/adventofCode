#!/usr/bin/local/python3

def detectGroup(stream):
    s = 0
    l = 0
    gbg = False
    ig = False
    #print(stream)
    for i in stream:
        #print(i,s,l,gbg,ig)
        if i == "!" and not ig:
            ig = True
            continue
        if ig:
            ig = False
            continue
        if i == "<":
            gbg = True
            continue
        if i == ">":
            gbg = False
            
        if i == "{" and not gbg:
            l += 1
        if i == "}" and not gbg:
            s += + l
            l -= 1
    return s
        

def main(s):
    print("*********")
    groups = detectGroup(s)
    print(groups)
    print()
    return groups

def test():
    print(main("{}"))
    print( main("{{{}}}"))
    print(main("{{},{}}"))
    print(main("{{{},{},{{}}}}"))
    print(main("{<a>,<a>,<a>,<a>}"))
    print(main("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
    print(main("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
    print(main("{{<a!>},{<a!>},{<a!>},{<ab>}}"))

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
#test()
part1()
puzzle_input()
