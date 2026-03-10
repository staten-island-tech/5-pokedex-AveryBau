import json 
pokedex = open("./pokedex.json", encoding = "utf8")
data = json.load(pokedex)

hm = int(input("What pokemon you want?"))
value = data[hm]
poke = []
print("name is", value)

print(data[0]["name"])
print(data[1]["name"])