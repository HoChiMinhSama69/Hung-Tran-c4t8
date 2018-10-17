maytinh={
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}
for x,y in maytinh.items():
    print(x,":",y)
print("SO MACBOOK CO TRONG KHO LA:", maytinh["MACBOOK"])
n=input("NHAP HANG MAY TINH BAN MUON TIM HIEU: ").upper()
if n in maytinh:
    print("SO MAY CON TRONG KHO:",maytinh[n])
else: 
    print("???????????????")
maytinh["TOSHIBA"]=10
print(maytinh)
n=input("HAY NHAP LOAI MAY TINH MOI VAO: ").upper()
m=input("HAY NHAP SO MAY LOAI MOI TRONG KHO: ")
if m.isdigit():
    m=int(m)
    maytinh[n]=m 
    print(maytinh)
else:
    print("??????????")
maytinh["MACBOOK"]-=2
maytinh["DELL"]+=10
print(maytinh)
for x,y in maytinh.items():
    print(x,":",y)
print("TONG SO MAY TINH TRONG KHO LA:",sum(maytinh.values()))
maytinh["FUJISU"]=15
maytinh["ALIENWARE"]=5
gia={
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 350,
    "TOSHIBA" : 600,
    "FUJISU" : 900,
    "ALIENWARE" : 1000
}
print("GIA CUA 1 MAY ASUS:",gia["ASUS"])
n=input("NHAP HANG MAY: ").upper()
if n in gia:
    print("GIA CUA 1 MAY",n,"LA:",gia[n])
else:
    print("??????????")
print("GIA CUA 5 MAY ASUS LA:",5*gia["ASUS"])
n=input("BAN MUON MUA MAY GI VA MUON MUA MAY CAI?? ")
if ":" in n:
    a=n.split(":")
    h=int(a[1])
    m=a[0].upper()
    if 0<h<maytinh[m]:
        print("DON HANG:", gia[m]*h)
    else:
        print("DEO DU MAY")
else:
    print("??")
empty=[]
for x in maytinh:
    n=maytinh[x]*gia[x]
    print("TONG GIA TRI CUA",x,":",n)
    empty.append(n)
print("TONG GIA TRI CUA CAC MAY LA:",sum(empty))
