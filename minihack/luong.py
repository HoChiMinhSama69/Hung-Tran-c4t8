bangluong = [
    {
    "name": "Huy",
    "role": "waiter",
    "hours": 12,
    "salary per hour": 0.8
    },
    {
    "name": "Tung",
    "role": "cook",
    "hours": 24,
    "salary per hour": 1.5
    },
    {
    "name": "M.Duc",
    "role": "manager",
    "hours": 20,
    "salary per hour": 2
    }
]
print(bangluong)
bangluong.append({
    "name": "Don",
    "role": "waiter",
    "hours": 12,
    "salary per hour": 0.9
})
bangluong.append({
    "name": "H.Duc",
    "role": "waiter",
    "hours": 14,
    "salary per hour": 0.7
})
print(bangluong)
print(bangluong[2]["salary per hour"])
bangluong[0]["name"]="Huyen"
bangluong[0]["role"]="waitress"
bangluong[0]["hours"]=14
bangluong[0]["salary per hour"]=1
print(bangluong[0])
bangluong.pop(4)
for p in bangluong:
    print("name:", p["name"])
    print("role:", p["role"])
    print("hours:", p["hours"])
    print("salary per hour:", p["salary per hour"])
    print("salary per month:", p["salary per hour"]*p["hours"]*30)
    print("__________________________")
    