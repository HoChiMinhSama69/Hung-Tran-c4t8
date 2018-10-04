while True:
    n=input("DIEN TEN DANG NHAP VAO: ")
    print(n)
    m=input("DIEN MAT KHAU VAO: ")
    if len(m)>8:
        if not m.isdigit() and not m.isalpha():
            b=input("NHAP LAI MAT KHAU: ")
            if m==b:
                a=input("DIEN EMAIL VAO: ")
                if "@" in a:
                    if ".com" in a:
                        print("XIN CHAO")
                        break
                    else:
                        print("DEO CO EMAIL DAY")
                else:
                    print("DEO CO EMAIL DAY")
            else:
                print("NHAP SAI ROI THANG OC CUT")
        else:
            print("MAT KHAU DEO PHONG PHU LAM ON NHAP NHIEU KY TU KHAC NHAU VAO")
    else:
        print("MAT KHAU KHONG DU KY TU")
            