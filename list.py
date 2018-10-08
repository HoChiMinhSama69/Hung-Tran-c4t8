# lit=[]
# print(lit)
# print(type(lit))

# lit=["con em phu nu viet nam"]
# print(lit)
# print(type(lit))

lit=["con em phu nu viet nam", "bác hồ", "các mác"]
print(lit)
print(type(lit))
lit.append("lenin")
print(lit)
sothichmoi=input("SO THICH MOI: ")
lit.append(sothichmoi)
print(lit)
print(*lit)
print(*lit, sep=", ")
print(*lit, sep=" | ")
print(lit[0].upper())
print(lit[-1].upper())
print(lit[-2].upper())
lit[0]="người nhện 2"
print(lit)
lit[-1]="sach tieng viet 10"
print(lit)
i=int(input("NHAP VI TRI VAO: "))
lit[i]=input("nhap noi dung vao: ")
print(lit)
if "LOL" in lit:
    lit.remove("LOL")
else:
    print("LOL DEO CO TRONG DANH SACH")
a=int(input("HAY NHAP VI TRI CUA THU BAN MUON XOA: "))
lit.pop(a)
print(lit)
b=int(input("HAY NHAP VI TRI CUA THU BAN MUON XOA: "))
lit.pop(b)
print(lit)
lit.append("QUYEN SO CHET")
lit.append("DIT ME PINOY")
lit.append("ssss")
for i, item in enumerate(lit):
    print(i + 1, item)
empty_list = []
for i, item in enumerate(lit):
    if "e" in item or "E" in item:
        empty_list.append(item)
print(empty_list)
while True:
    n=input("C, R, U HAY D??!?")
    if n=="C":
        m=input("NHAP SO THICH MOI VAO: ")
        lit.append(m)
        print(lit)
    elif n=="R":
        if lit==[]:
            print("DANH SACH TRONG")
        else:
            for i, item in enumerate(lit):
                print(i+1, item)
    elif n=="U":
        x=int(input("NHAP VI TRI VAO: "))
        lit[x]=input("nhap noi dung vao: ")
        print(lit)
    elif n=="D":
        print(lit)
        y=int(input("NHAP VI TRI CUA THU BAN MUON XOA: "))
        lit.pop(y)
        print(lit)
    else:
        print("CHON 1 TRONG 4 CHU CAI DIT CU MAY")


