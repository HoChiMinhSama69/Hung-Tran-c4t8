list1=["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
list2=[150300, 247100, 333300, 266800, 420900, 318000]
print("DANH SÁCH DÂN SỐ CỦA CÁC QUẬN:")
for x in range(len(list1)):
    print(list1[x], list2[x])
print("DÂN SỐ LỚN NHẤT:", max(list2))
print("=> QUẬN ĐĐ CÓ DÂN SỐ LỚN NHẤT")
print("DÂN SỐ NHỎ NHẤT:", min(list2))
print("=> QUẬN ST CÓ DÂN SỐ NHỎ NHẤT")
list3=[117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
list4=[]
for x in range(len(list1)):
    a=list2[x]/list3[x]
    list4.append(a)
print("DANH SÁCH MẬT ĐỘ DÂN CƯ CỦA CÁC QUẬN:")
for x in range(len(list1)):
    print(list1[x], list4[x])
print("MẬT ĐỘ DÂN CƯ TRUNG BÌNH CỦA CÁC QUẬN:", sum(list4)/len(list1))