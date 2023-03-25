from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")

# select database and collection
db = client["GSoC21"]
collection = db["CommentsREAL"]

# add a new field to all documents in the collection
collection.update_many({}, {"$set": {"GSoC": "2021"}})