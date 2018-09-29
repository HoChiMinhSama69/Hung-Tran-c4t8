while True:
    n=input("NHAP MAT KHAU ")
    if n.isalpha():
        print("SAI ROI")
    else:
        if len(n) <=8:
            print("DUNG ROI DO")
            break
        else:
            print("SAI ROI")
