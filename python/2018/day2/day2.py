
def part1():
    s_2s= 0
    s_3s= 0
    for line in open("input.txt","r"):
        freqs = {}
        for letter in line:
            if letter in freqs:
                freqs[letter] += 1
            else:
                freqs[letter] = 1
        print(freqs)
        if 2 in freqs.values():
            s_2s += 1
        if 3 in freqs.values():
            s_3s += 1
        print("2s:",s_2s, "3s", s_3s)
    print("checksum:", (s_2s*s_3s))


def part2():
    listline = []
    for line in open("input.txt","r"):
        listline.append(list(line))
    
    for a in listline:
        for b in listline:
            inters= [i for i, j in zip(a, b) if i != j]
            if len(inters) == 1:
                print(''.join(a))
                print(''.join(b))
                print(inters)
                exit()

if __name__ == "__main__":
    part1()
    part2()