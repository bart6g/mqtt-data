from pymongo import MongoClient
import pymongo
import json

client = MongoClient(
    'string')
db = client.mqtt
col = db["sensors"];
tempSensors = []
humSensors = []
dogSensors = []

for x in col.find({'topic': 'humidity'}):
    id = x['_id']
    # print(x)
    # print(id)
    humSensors.append(id)

print(humSensors)
