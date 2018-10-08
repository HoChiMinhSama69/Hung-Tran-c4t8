from random import *
n=input("NHAP 1 CHU VAO: ")
m=list(n)
empty=[]
for x in n:
    a=choice(m)
    m.remove(a)
    empty.append(a)
for x in empty:
    print(x)