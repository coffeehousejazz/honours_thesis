import requests, json, time
from pymongo import MongoClient
# this code puts the pulls from users in the db
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
src_db = myclient["GSoC"]
src_col = src_db["Users3"]
# db redesigns

# API AUTHENTICATION
me_user = 'coffeehousejazz'
token = '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'

counter = 0
# grab user data (read str)
for coll in src_db.list_collection_names():
    Collection = src_db[coll]
    users = list(Collection.find({"$or": [{"mentee": True}, {"mentor": True}]}))
    counter += 1
    for x in users:
        # add an id to pair mentors and mentees
        x['pair_id'] = counter
    print(users)
    src_col.insert_many(users)
    #if isinstance(users, list):
    #    src_col.insert_many(users)
    #else:
    #    src_col.insert_one(users)

# close the connection
myclient.close()