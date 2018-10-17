book={
    "name": "lakad matatag",
    "release date": 1987,
    "cast": ["putang", "ina", "bobo"]
}
print(book)
book["country"]="phi líp pin"
book["publisher"]="normalin"
for x in book:
    print(x,":")
    print(book[x])
    print("-")
book["cast"]=["thơ nguyễn", "angelina jolie", "iiiiiiii"]
print(book)
book["cast"].append("kakakaka")
print(book)
book["cast"].pop(3)
print(book)
print(book["cast"][1])
for x in book["cast"]:
    print(x)
for x,y in book.items():
    print(x, ":", y)
