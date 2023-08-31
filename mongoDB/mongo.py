import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb = myclient["S202DB"]

myCollection = myDb["customers"]
