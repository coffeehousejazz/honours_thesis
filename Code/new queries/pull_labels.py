from pymongo import MongoClient
# pull request labels
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
counter = 0
Collection = db["Pulls"]
cur = Collection.find({"pr/issue": True, "closed_at":{"$ne":None}}, 
                    {"number": 1, "labels.name":1})

# define the aggregation pipeline
#groups all of the documents by mentee and gets all the labels for the prs
# should be MENTEE_NAME NOT MENTEE
pipeline = [
    {"$group": {
        "_id": "$mentee",
        "field": {"$push": "$labels.name"}
     }}
]

# perform the aggregation
results = Collection.aggregate(pipeline)

# print the results
# cursor that is a dictionary that has the mentee and all the lables
for result in results:
    print(result)
    print("_________")