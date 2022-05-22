import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017"
database = mongoClient["College"]
collections = database["departments"]
depatData = {"name":"IT", "id":1001}

collections.insert_one(depatData)