while True:
    n=input("NHAP MAT KHAU ")
    if n.isalpha():
        print("SAI")
    else:
        if len(n) <=8:
            if n.istitle():
                print("DUNG")
                break
            else:
                print("SAI")
        else:
            print("SAI")