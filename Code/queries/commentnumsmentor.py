from pymongo import MongoClient
# number of comments by mentor
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
counter = 0
for coll in db.list_collection_names():
    Collection = db[coll]
    cur = Collection.find({"pr/issue": True, "closed_at":{"$ne":None}}, {"number": 1})
    closed_nums = []
    for x in cur:
        print(x) 
        for key in x:
            if key == "number":
                closed_nums.append(x[key])
    # find username
    username = Collection.find_one({"mentor":True}, {"login": 1})
    # print(username)
    name = ''
    for key in username:
            if key == "login":
               name = username[key]
    print(name)
    # find comments that are closed and have username
    for i in closed_nums:
        cur = Collection.find({"comment": True, "user.login": name, "issue_url": {"$regex": str(i)}})
        for x in cur:
            print(x)
            counter += 1
    print(counter)