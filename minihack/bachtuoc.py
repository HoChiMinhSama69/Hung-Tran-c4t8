bachtuoc={
    1 : "1 chân",
    2 : "2 chân",
    3 : "4 chân",
    4 : "8 chân"
}
empty=[]
print("BACH TUOC CO BAO NHIEU CHAN???!?")
for x,y in bachtuoc.items():
    print(x, ".", y)
n=input("CAU TRA LOI CUA BAN LA: ")
if n.isdigit():
    m=int(n)
    if m==1 or m==2 or m==3:
        print("SAI ROI DIT ME HOC LOP MAY DAY")
    elif m==4:
        print("DUNG ROI KHON DAY")
        empty.append(m)
    else:
        print("????????")
else:
    print("?????????????????????????????")
doggy={
    1 : "gau",
    2 : "meo",
    3 : "dit me may",
    4 : "tang ina"
}
print("CHO KEU TIENG GI?????!?")
for x, y in doggy.items():
    print(x, ".", y)
n=input("CAU TRA LOI CUA BAN: ")
if n.isdigit():
    m=int(n)
    if m==1 or m==2 or m==3:
        print("SAI ROI THANG NGU")
    elif m==4:
        print("DUNG ROI!!!")
        empty.append(m)
    else:
        print("????")
else:
    print("????????????????????")
print("SO CAU HOI BAN TRA LOI DUNG LA:", len(empty))
print("PHAN TRAM TRA LOI DUNG CUA BAN LA:", (len(empty)/2)*100, "%")