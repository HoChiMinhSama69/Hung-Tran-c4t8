lit=["red", "orange", "yellow"]
print("CAC MAU:")
print(*lit,sep=", ")
a=input("NHAP MAU MOI: ")
lit.append(a)
print("DANH SACH MAU MOI:")
print(*lit,sep=", ")
n=int(input("NHAP VI TRI VAO: "))
if (-(len(lit))) < n < (len(lit)):
    print(lit[n])
else:
    print("DEO CO VI TRI DAY")
m=input("NHAP THU BAN MUON XOA: ")
if m.isdigit():
    g=int(m)
    if (-(len(lit)))<g<(len(lit)):
        lit.pop(g)
        print(*lit,sep=", ")
    else:
        print("DEO CO VI TRI DAY")
elif m.isalpha():
    if m in lit:
        lit.remove(m)
        print(*lit,sep=", ")
    else:
        print("DEO CO CAI DAY TRONG LIST")
else:
    print("LAM CAI TRO LON GI DAY???!?")
from turtle import *
speed(0)
colors=["red","orange","yellow",a]
for x in colors:
    color(x)
    forward(40)

mainloop()
        
    
