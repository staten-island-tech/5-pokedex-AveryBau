import json 
pokedex = open("./pokedex.json", encoding = "utf8")
data = json.load(pokedex)
""" 
choice = int(input("Write name of a pokemon"))
value = data[choice]
poke = []
print("name is", value)
language = input(("What language?"))
print(data[choice]["name"][language])
 """
new = input("What type of pokemon do you want?")
list = []
for mon in data: 
    if new in mon["type"]:
        print(mon)


""" print(data[0]["name"]
print(data[1]["name"]) """