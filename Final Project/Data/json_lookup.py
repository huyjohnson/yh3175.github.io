import json

# Opening JSON file
f = open("allcounties_import.json",)

# returns JSON object as a dictionary
data = json.load(f)

#Iterating through the json list
for i in data["features"]:
    print(i)
