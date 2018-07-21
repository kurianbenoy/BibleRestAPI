import json
import random

from django.shortcuts import render
from django.http import JsonResponse

with open('bible.json') as f:
    data = json.load(f)



def randomverse(request):
        for item in data["Book"]:
            for chapter in item["Chapter"]:
                for verse in chapter["Verse"]:
                    a = verse["00000007"]
