diction = {}
print(diction == {})
diction1={
    "name": "mga bobo"
}
print(diction1)
diction2={
    "name": "mga bobo", 
    "age": 20
}
print(diction2)
diction3={
    "name": "hồ chí minh",
    "description": "rất đẹp zai",
    "occupation": "cứu nước"
}
print(diction3)
diction3["năm mất"]=1969
print(diction3)
diction3[input("NHẬP KEY VÀO: ")]=input("NHẬP VALUE VÀO: ")
print(diction3)
print(diction3["name"], diction3["description"])
n=input("NHẬP KEY VÀO: ")
if n in diction3:
    print(diction3[n])
else:
    print("ĐÉO CÓ KEY ĐẤY ĐỊT CỤ M")
diction3["description"]="rất đẹp zai, râu ria lành mạnh"
n = diction3["description"]
print(diction3)
b = input("NHẬP VALUE VÀO: ")
l = n + ", " + b
diction3["description"]= l
print(diction3)
del diction3["description"]
print(diction3)
m=input("NHẬP KEY BẠN MUỐN XÓA: ")
if m in diction3:
    del diction3[m]
    print(diction3)
else:
    print("ĐÉO CÓ DCMM")
if "name" in diction3:
    print("key name exists")
else:
    print("key name doesn't exist")
if "nationality" in diction3:
    print("key nationality exists")
else:
    print("key nationality doesn't exist")
diction4={
    "poop": "cứt",
    "vagina": "lồn",
    "communist life is so awesome!!!": "cuộc đời cách mạng thật là sang!!"
}
print(diction4)
n=input("TRA CỨU TỪ ĐIỂN: ")
if n in diction4:
    print(diction4[n])
else:
    print("ĐÉO CÓ TRONG TỪ ĐIỂN")
while True:
    n=input("TRA CỨU HAY KHÔNG??!? ").lower()
    if n=="có":
        m=input("TRA CỨU: ").lower()
        if m in diction4:
            print(diction4[m])
        else:
            print("ĐÉO CÓ TRONG TỪ ĐIỂN")
    elif n=="không" or n=="ko":
        break
    else:
        print("?????????")