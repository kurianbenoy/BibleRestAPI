import json
from pprint import pprint


with open('malayalmbible.json') as f:
    data = json.load(f)



for item in data["Book"]:
    for chapter in item["Chapter"]:
        for verse in chapter["Verse"]:
            if(verse["Verseid"] == 00000000):
                pprint(verse["Verse"])
