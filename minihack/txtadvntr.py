character={
    "name" : "senjo",
    "age" : 26,
    "strength" : 18,
    "defense" : 1,
    "HP" : 200,
    "backpack" : ["dildo", "fleshlight"],
    "gold" : 200,
    "level" : 6
}
print(character)
character["gold"]+=50
print(character["gold"])
character["backpack"].append("flintstone")
print(character["backpack"])
character["pocket"]=["monsterDex", "flashlight"]
print(character)
skill1={
    "name" : "DIT",
    "minimum lvl" : 1,
    "damage" : 600,
    "hit rate" : 0.5
}
skill2={
    "name" : "VAI LON",
    "minimum lvl" : 5,
    "damage" : 444,
    "hit rate" : 0.8
}
empty={}
empty["1."]=skill1["name"]
empty["2."]=skill2["name"]
print("1.",skill1["name"])
del skill1["name"]
for x,y in skill1.items():
    print(x,":",y)
print("-----------")
print("2.",skill2["name"])
del skill2["name"]
for x,y in skill2.items():
    print(x,":",y)
print("ENEMY DETECTED, COMMENCING COMBAT:")
for x,y in empty.items():
    print(x,y)
n=(input("CHOOSE WHICH SKILL TO USE: "))
if n.isdigit():
    n=int(n)
    import random
    if n==1:
        if character["level"]>=skill1["minimum lvl"]:
            m=random.uniform(0,1)
            if m>skill1["hit rate"]:
                print("SUCCESSFUL HIT, YOU'VE DEALT",skill1["damage"],"DAMAGE")
            else:
                print("MISSED")
        else:
            print("INSUFFICIENT LEVEL")
    elif n==2:
        if character["level"]>=skill2["minimum lvl"]:
            m=random.uniform(0,1)
            if m>skill2["hit rate"]:
                print("SUCCESSFUL HIT, YOU'VE DEALT",skill2["damage"],"DAMAGE")
            else:
                print("MISSED")
        else:
            print("INSUFFICIENT LEVEL")
    else:
        print("???")
else:
    print("???????????????????????")
        


