from pymongo import MongoClient
# pull request labels
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
counter = 0
for coll in db.list_collection_names():
    Collection = db[coll]
    cur = Collection.find({"pr/issue": True, "closed_at":{"$ne":None}}, 
                          {"number": 1, "labels.name":1})
    closed_nums = []
    for x in cur:
        for key in x:
            if key == "labels":
                print(x[key])