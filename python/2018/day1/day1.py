
def main():
    s = 0
    freqs = []
    while 1:
        for line in open("input.txt","r"):
            s += int(line)
            if s in freqs:
                print("repeated",s)
                exit(0)
            freqs.append(s)
        print("sum",s)

if __name__ == "__main__":
    main()