import requests
from pymongo import MongoClient
# get other repos that the mentee was in

#github api token
username = 'coffeehousejazz'
token = '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'

myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
counter = 0
for coll in db.list_collection_names():
    Collection = db[coll]
    # find username
    name = Collection.find_one({"mentee":True}, {"login": 1})
    # print(username)
    for key in name:
            if key == "login":
               name2 = name[key]
    mentee_url = f"https://api.github.com/users/{name2}/repos"
    response = requests.get(mentee_url, auth=(username, token))
    if response.status_code == 200:
        data = response.json()
        for repo in data:
            # print(repo["owner"])
            print(repo["name"])
    print("_______")