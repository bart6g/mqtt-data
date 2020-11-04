from pymongo import MongoClient
from bson import ObjectId
import pymongo
import json


client = MongoClient(
    'string')
db = client.mqtt


col = db["sensors"];
tempSensors = []
humSensors = []
dogSensors = []

for x in col.find({'topic': 'dogfood'}):
    id = x['_id']
    # print(x)
    # print(id)
    dogSensors.append(str(id))
for x in col.find({'topic': 'dogfood'}):
    id = x['_id']
    # print(x)
    # print(id)
    tempSensors.append(str(id))
for x in col.find({'topic': 'dogfood'}):
    id = x['_id']
    # print(x)
    # print(id)
    humSensors.append(str(id))

def tempHandler(jsonData):

    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']

    Data_and_Time = json_Dict['Date']
    Temperature = json_Dict['Temperature']
    toSave = {"sensorId": ObjectId(SensorID),
              "date": Data_and_Time, "temp": Temperature}

    db.temperature.insert_one(toSave)
    print("zapisany w bazie temp id: " + str(SensorID))


def humHandler(jsonData):
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']
    Data_and_Time = json_Dict['Date']
    Humidity = json_Dict['Humidity']
    toSave = {"sensorId": ObjectId(SensorID),
              "date": Data_and_Time, "humidity": Humidity}

    db.humidity.insert_one(toSave)
    print("zapisany w bazie humidity id: " + str(SensorID))


def dogFoodHandler(jsonData):
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']
    Data_and_Time = json_Dict['Date']
    DogFood = json_Dict['DogFood']
    toSave = {"sensorId": ObjectId(SensorID),
              "date": Data_and_Time, "dogFood": DogFood}

    db.dogFood.insert_one(toSave)
    print("zapisany w bazie dogfood id: " + str(SensorID))

def sensor_Data_Handler(Topic, jsonData):

    if Topic == "Home/BedRoom/DHT22/Temperature":
        tempHandler(jsonData)
    elif Topic == "Home/BedRoom/DHT22/Humidity":
        humHandler(jsonData)
    elif Topic == "Home/BedRoom/DHT22/DogFood":
        dogFoodHandler(jsonData)
