from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")

# select database and collection
db = client["GSoC"]
collection = db["Users"]

# update the text field in all documents by appending 'a'
collection.update_many({}, {"$set": {"pair_id": {"$concat": [{"$toString": "$pair_id"}, ".1"]}}})