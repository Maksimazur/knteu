import json

from valute import list1
from exchange_rate import list2

def convertToJSON():
    with open("D:\Python\TheEnd\ list1_json.json", "w") as write_file:
        json.dump(list1, write_file)

def convertInJSON():
    with open("D:\Python\TheEnd\list2_json.json", "w") as write_file:
        json.dump(list2, write_file)