while True:
    n=input("NHAP SO VAO DAY: ")
    if n.isdigit():
        g=int(n)
        print(g**2)
        break
    else:
        print("DAY DEO PHAI LA SO")