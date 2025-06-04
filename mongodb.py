from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.Registros

people = db.people

people.insert_one({"name": "Evandro", "age": "19"})

for person in people.find():
    print(person)
