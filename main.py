from random import shuffle
import openpyxl
import json
from datetime import datetime, timedelta

members = [
    "Sis Peace",
    "Bro Tosin",
    "Bro Ayo",
    "Bro Victor",
    "Sis Tolu",
    "Bro Fiyin",
    "Sis Bukola",
    "Bro Lanre",
    "Bro Alex",
    "Bro Jonathan",
    "Bro Ebun",
    "Bro Eni",
]

comb_list = []
# we need to select two of the media guys
for i in range(2):
    media_guys = members[-2:]
    not_media_guys = [*members[:-2]]
    print(not_media_guys, media_guys)
    for j in range(len(not_media_guys)):
        comb_list.append([media_guys, list(filter(lambda x: not_media_guys.index(x) != j, not_media_guys))])



def get_week_dates():
    today = datetime.today()
    count = 0
    while True:
        monday = today + timedelta(days=(count + 1))
        thursday = today + timedelta(days=(count + 4))
        sunday = today + timedelta(days=(count + 7))
        yield monday.isoformat().split('T')[0], \
            thursday.isoformat().split('T')[0], \
            sunday.isoformat().split('T')[0]
        count += 7 
    
data = {}
date_gen = get_week_dates()
for i in range(2):
    for lis in comb_list:
        media, non_media = lis
        shuffle(media)
        shuffle(non_media)
        monday, thursday, sunday = next(date_gen)

        data = {
            **data,
            monday : {
                "stage" : non_media[0],
                "recording" : media[0],
                "mixer" : non_media[1]
            },
            thursday: {
                "stage" : non_media[2],
                "mixer" : non_media[3],
            },
            sunday: {
                "stage" : non_media[4:6],
                "recording" : media[1],
                "mixer" : non_media[6:-1]
            }
        }


# save the data to a json file

json.dump(data, open("data.json", "w"))