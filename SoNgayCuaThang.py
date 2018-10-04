while True:
    n=int(input("NHAP THANG VAO: "))
    if n in (1,3,5,7,8,10,12):
        print(n, "CO 31 NGAY")
        break
    elif n==2:
        print(n, "CO 28 HOAC 29 NGAY")
        break
    elif n in (4,6,9,11):
        print(n, "CO 30 NGAY")
        break
    else:
        print("DEO CO THANG DAY THANG NGU")
