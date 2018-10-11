lit=[12,214,69,87]
print("HIGH SCORES:")
for i, item in enumerate(lit):
    print(i+1, item)
a=sorted(lit, reverse=True)
print("HIGH SCORES FROM HIGHEST TO LOWEST:")
for i, item in enumerate(a):
    print(i+1, item)
n=int(input("ENTER YOUR NEW HIGH SCORE: "))
lit.append(n)
print("HIGH SCORES:")
for i, item in enumerate(lit):
    print(i+1, item)
b=sorted(lit, reverse=True)
print("HIGH SCORES FROM HIGHEST TO LOWEST:")
for i, item in enumerate(b):
    print(i+1, item)
lit2=[18,99,67,100,345,25,66]
g=sorted(lit2, reverse=True)
print("HIGH SCORES FROM HIGHEST TO LOWEST:")
for x in range(5):
    print(x+1, g[x])
m=int(input("ENTER YOUR NEW HIGH SCORE: "))
lit2.append(m)
print("HIGH SCORES FROM HIGHEST TO LOWEST:")
h=sorted(lit2, reverse=True)
for x in range(5):
    print(x+1, h[x])