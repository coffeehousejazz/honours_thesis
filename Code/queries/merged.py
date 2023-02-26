from pymongo import MongoClient
# collect numbers from merged PRs
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
counter = 0
for coll in db.list_collection_names():
    Collection = db[coll]
    cur = Collection.find({"pr/issue": True, "closed_at":{"$ne":None}, "pull_request.merged_at":{"$ne":None}}, {"number": 1})
    closed_nums = []
    for x in cur:
        print(x) 
        for key in x:
            if key == "number":
                closed_nums.append(x[key])
    for i in closed_nums:
        print(i)
        counter += 1
print(counter)