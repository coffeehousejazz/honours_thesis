from pymongo import MongoClient
from datetime import datetime
# this code adds the mentees names on the mentors so we know who goes with who
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC"]
for coll in db.list_collection_names():
    Collection = db[coll]
    # prints the first item in the collection
    # for x in Collection.find({"login":{"$exists":True}}):
    #for x in Collection.find({}, {"login":1, "followers":1, "following":1, "location":1, "created_at":1}):
    print(Collection)
    x = Collection.find_one()
    print(x)
    for key in x:
        if key == "_id":
            id_num = x[key]
    print(id_num)
    Collection.update_one({'_id':id_num}, {"$set": {"mentee": True}})
    Collection.update_one({'_id':id_num}, {"$set": {"mentor": False}})
