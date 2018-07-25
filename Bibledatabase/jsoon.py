import json
import pandas as pd
from pprint import pprint


with open('malayalmbible.json') as f:
    data = json.load(f)



for item in data["Book"]:
    for chapter in item["Chapter"]:
            df = pd.DataFrame(chapter["Verse"])
            genr = 65021020
            a = df["Verseid"]
            # if a == genr:
            #     print(df.loc(a))
            print(a)
