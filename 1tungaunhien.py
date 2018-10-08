from random import *
lit=["cong san", "muon nam"]
m=choice(lit)
a = list(m)
shuffle(a)
for x in a:
    print(x)
n=input("HAY DOAN CHU: ")
if n==m:
    print("DUNG ROI")
else:
    print("SAI DIT CU MAY")