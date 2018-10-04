while True:
    import random
    m=random.randint(0,100)
    n=random.randint(0,100)
    f= m + n + random.randint(-1,1)
    print(m,"+",n,"=",f)
    b=(input("DUNG HAY SAI "))
    if f==m+n:
        if b=="DUNG":
            print("CHINH XAC")
        else:
            print("SAI ROI")
            break
    else:
        if b=="SAI":
            print("CHINH XAC")
        else:
            print("SAI ROI")
            break
        