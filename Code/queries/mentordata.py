from pymongo import MongoClient
# mentor demographics
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
for coll in db.list_collection_names():
    Collection = db[coll]
    cur = Collection.find({"mentor": True}, {"login": 1, "location": 1, "followers": 1,
                                             "following": 1, "public_repos": 1, "company":1,
                                             "public_gists": 1, "created_at": 1})
    for x in cur:
        print(x)