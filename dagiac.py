from turtle import *
speed(0)
color("brown")
n=int(input("NHAP SO CANH VAO "))
for x in range(n):
    forward(100)
    left(360/n)
mainloop()