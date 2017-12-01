#!/usr/local/bin/python3


def calc(in_list):
    sum = 0
    step = int(len(in_list)/2)
    for i in range(len(in_list)):
        curr = in_list[i]

        if (i+step) >= len(in_list)-1:
            idx = (i+step) - len(in_list)
            nextd = in_list[idx]
        else:
            nextd = in_list[i+step]


        if curr == nextd:
            sum += int(curr)
        
    return sum

assert 6 == calc("1212")
assert  0 == calc("1221")
assert 4 == calc("123425")
assert 12 == calc("123123")
assert 4 == calc("12131415")
