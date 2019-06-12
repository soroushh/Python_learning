dict = {
"name":"soroush",
"family": "khosravi"
}

print(dict)

a = dict.get("name")

print(a)

for i in dict:
    print(i)

print(len(dict))

for x,y in dict.items():
    print(x +" "+ y)
    
for b in dict.values():
    print(b)
