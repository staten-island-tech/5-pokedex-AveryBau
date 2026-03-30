import json 
pokedex = open("./pokedex.json", encoding = "utf8")
data = json.load(pokedex)

""" choice = int(input("What pokemon do you want? (Write name)"))
value = data[choice]
poke = []
print("name is", value)
language = input(("What language?"))
print(data[choice]["name"][language])

new = input("What type of pokemon do you want?")
for mon in data: 
    if new in mon["type"]:
        print(mon["name"])
else:
    print("What the heck is that")  """

""" huh = input("What kind of pokemon do you want?")
for mon in data:
    if huh in mon["name"]["english"]:
        print(mon["name"]["english"])
else:
    print("No pokemon for you")

poke = open("./moves.json", encoding="utf8")
moves = json.load(poke)
uhh = input("What type of pokemon do you want to show the moves available")
for mon in moves:
    if uhh in mon["type"]:
        print(mon["ename"])
else:
    print("no moves")

""" print(data[0]["name"]
print(data[1]["name"]) """