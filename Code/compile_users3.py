from pymongo import MongoClient
# this code compiles all the users(mentors and mentees) together into one collection
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
src_db = myclient["GSoC"]
src_col = src_db["Users"]
counter = 0.1
# grab user data (read str)
for coll in src_db.list_collection_names():
    Collection = src_db[coll]
    users = list(Collection.find({"$or": [{"mentee": True}, {"mentor": True}]}))
    counter += 1
    for x in users:
        x['pair_id'] = counter
        src_col.insert_one(x)

# close the connection
myclient.close()