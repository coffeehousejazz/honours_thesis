from pymongo import MongoClient
# mentee demographics
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
for coll in db.list_collection_names():
    Collection = db[coll]
    cur = Collection.find({"mentee": True})
    for x in cur:
        print(x)