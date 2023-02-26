from pymongo import MongoClient
# this code updates the mentees so that they are annotated! :))
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
counter = 0
for coll in db.list_collection_names():
    Collection = db[coll]
    cur = Collection.find({
    "$and": [
        {"followers_url": {"$exists": True}},
        {"organizations_url": {"$exists": True}}
    ]
    })
    for x in cur:
        counter += 1
        for key in x:
            if key == "_id":
                id_num = x[key]
                print(id_num)
                Collection.update_one({'_id':id_num}, {"$set": {"mentee": False}})
                Collection.update_one({'_id':id_num}, {"$set": {"mentor": True}})
                Collection.update_one({'_id':id_num}, {"$set": {"pr/issue": False}})
                Collection.update_one({'_id':id_num}, {"$set": {"comment": False}})
print(counter)
# go to each of the files and add the mentee: mentor: pr/issue: comment: fields
# Collection.update_one({'_id':object_nums[0]}, {"$set": {"mentee": True}})

    # print("db: {}, collection:{}".format(db, coll))
    # for r in db[coll].find({}):
    #    print(r)
    #    print('\n\n')
