from pymongo import MongoClient
from datetime import datetime
counter = 0
# do it in a for loop to iterate through all of the collections
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
counter = 0
count = 0
for coll in db.list_collection_names():
    counter += 1
    Collection = db[coll]
    # comments do not have events_url or name
    # cur = Collection.find({"events_url": { "$exists": False}})
        
    cur = Collection.find_one({
    "$and": [
        {"comments_url": {"$exists": True}},
        {"events_url": {"$exists": True}}
    ]
    })
    #print(cur)
    owner_name = ""
    repo_name = ""
    for x in cur or []:
            if x == "url":
                id_num = cur[x]
                print(id_num)
                start = id_num.find("/repos/") + len("/repos/")
                end = id_num.find("/issues/")
                new_string = id_num[start:end]
                print(id_num[start:end])
                
                parts = new_string.split("/")
                owner_name = parts[0]
                repo_name = parts[1]
                count += 1
                #Collection.update_one({'_id':id_num}, {"$set": {"mentee": False}})
                #Collection.update_one({'_id':id_num}, {"$set": {"mentor": False}})
                #Collection.update_one({'_id':id_num}, {"$set": {"pr/issue": True}})
                #Collection.update_one({'_id':id_num}, {"$set": {"comment": False}})
    users = Collection.find({"$or": [{"mentee": True}, {"mentor": True}]})
    for x in users:
        for key in x:
            if key == "_id":
                id_num2 = x[key]
                print(owner_name)
                print(repo_name)
                Collection.update_one({'_id':id_num2}, {"$set": {"owner_name": owner_name}})
                Collection.update_one({'_id':id_num2}, {"$set": {"repo_name": repo_name}})
    print(counter)
    #print(owner_name)
    #print(repo_name)