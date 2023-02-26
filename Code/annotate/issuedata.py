from pymongo import MongoClient
from datetime import datetime

# do it in a for loop to iterate through all of the collections
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC"]
counter = 0
count = 0
for coll in db.list_collection_names():
    Collection = db[coll]
    # comments do not have events_url or name
    # cur = Collection.find({"events_url": { "$exists": False}})
    cur = Collection.find({
    "$and": [
        {"comments_url": {"$exists": True}},
        {"events_url": {"$exists": True}}
    ]
    })
    for x in cur:
        print(x)
        counter += 1
        for key in x:
            if key == "_id":
                id_num = x[key]
                print(id_num)
                count += 1
                #Collection.update_one({'_id':id_num}, {"$set": {"mentee": False}})
                #Collection.update_one({'_id':id_num}, {"$set": {"mentor": False}})
                #Collection.update_one({'_id':id_num}, {"$set": {"pr/issue": True}})
                #Collection.update_one({'_id':id_num}, {"$set": {"comment": False}})
   
    print(counter)
    print(count)