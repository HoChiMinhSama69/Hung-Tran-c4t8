lit=[1,11,69,8,-22]
flag = False
position = 854545
n=int(input("NHAP 1 SO VAO: "))
for i, item in enumerate(lit):
    if item==n:
        position = i
        flag = True
if flag == True:
    print("CO TRONG DANH SACH, VI TRI SO", position)
else:
    print("DEO CO TRONG DANH SACH")
print("CACH DUNG sum(): ")
print("TONG CUA DAY SO LA", sum(lit))
print("CACH KHONG DUNG sum(): ")
a=0
for x in lit:
    a+=x
    print(a)
print("TONG CUA DAY SO LA SO CUOI CUNG")
m=(input("NHAP 1 DAY SO CO 5 CHU SO VAO, CAC SO CACH NHAU BOI DAU CACH: "))
if m.count(" ") == 4:
    g=m.split(" ")
    g=[int(x) for x in g]
    print("TONG CUA 5 SO VUA NHAP LA: ",sum(g))
else:
    print("CHUA DU 5 SO DIT ME MAY")
empty=[]
for x in lit:
    if x%2==0:
        empty.append(x)
print("CAC SO CHAN TRONG DANH SACH:")
print(*empty,sep=", ")
k=input("NHAP 1 DAY SO CO 5 CHU SO, CACH NHAU BOI DAU ,: ")
bempty=[]
if k.count(",")==4:
    l=k.split(",")
    l=[int(x) for x in l]
    for x in l:
        if x%2==0:
            bempty.append(x)
    print("CAC SO CHAN TRONG DANH SACH CUA BAN:")
    print(*bempty,sep=", ")
else:
    print("CHUA DU 5 SO DIT ME MAY")
