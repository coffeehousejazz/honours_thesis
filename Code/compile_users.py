from pymongo import MongoClient
# this file compiles all the users(mentors and mentees) together into one collection
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
src_db = myclient["GSoC21"]
dst_db = myclient["GSoC-redesign"]
src_col = src_db["Users"]
dst_collection = dst_db["Users"]

# grab user data (read str)
for coll in src_db.list_collection_names():
    Collection = src_db[coll]
    users = list(Collection.find({"$or": [{"mentee": True}, {"mentor": True}]}))
    src_col.insert_many(users)

# close the connection
myclient.close()