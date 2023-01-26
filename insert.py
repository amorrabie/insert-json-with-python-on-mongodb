import json
from pymongo import MongoClient
#import pymongo

with open('dump.json') as f:
  data = json.load(f)

client = pymongo.MongoClient("mongodb://135.125.203.95:27017/")
mydb = client["admin"]
mycol = mydb["enda_info"]  


x = mycol.insert_one(data)

for y in mycol.find():
  print(y) 
