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
