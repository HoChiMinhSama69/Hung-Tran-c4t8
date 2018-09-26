import math
def pt(a,b,c):
    d=(b**2)-(4*a*c)
    if d>0:
        x1=(-b+math.sqrt(d))/(a*2)
        x2=(-b-math.sqrt(d))/(a*2)
        print("2 NGHIEM PHAN BIET!!")
        print("x1 =",x1)
        print("x2 =",x2)
    elif d==0:
        x=-b/(a*2)
        print("NGHIEM KEP!!")
        print("x =",x)
    else:
        print("VO NGHIEM EM OI")
print("NHAP a,b,c VAO OK")
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
if a==0:
    print("LOI ROI EM OI")
else:
    pt(a,b,c)