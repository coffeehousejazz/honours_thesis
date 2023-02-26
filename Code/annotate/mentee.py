from pymongo import MongoClient
from datetime import datetime
# this code updates the mentees so that they are annotated! :))
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
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

# go to each of the files and add the mentee: mentor: pr/issue: comment: fields
# Collection.update_one({'_id':object_nums[0]}, {"$set": {"mentee": True}})

    # print("db: {}, collection:{}".format(db, coll))
    # for r in db[coll].find({}):
    #    print(r)
    #    print('\n\n')
