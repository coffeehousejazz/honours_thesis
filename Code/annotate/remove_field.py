from pymongo import MongoClient

# Connect to MongoDB
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")

# Choose database and collection
db = myclient['Data']
mycollection = db['Users']

# Remove the field from all documents in the collection
mycollection.update_many({}, {"$unset": {"": 1}})

print("finished")