a = 883
b = 879

#a=65
a_f=16807

#b=8921
b_f=48271

def calc(num,fac):
    return ((num *fac) % 2147483647) 

A = a
B= b
match = 0
A = calc(A, a_f)
B = calc(B, b_f)
i=0
while i < 5000000:
    if A % 4 != 0:
        A = calc(A, a_f)
        continue
    while B % 8 != 0:
        B = calc(B, b_f)
    #print(A)
    #print(B)
    abin = bin(A).replace('0b','').zfill(32)
    bbin = bin(B).replace('0b','').zfill(32)
    if abin[16:32] == bbin[16:32]:
        match +=1
    #print("  ", A,B,"\r",end='')
    #print()

    A = calc(A, a_f)
    B = calc(B, b_f)
    print("  ", i,"match:",match,"\r",end='')
    i +=1

print()    
print("match:", match)
