from pymongo import MongoClient
# counts how many pull requests are merged
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
Collection = db["Pulls"]

# should be MENTEE_NAME NOT MENTEE
pipeline_merged = [
    {"$match": {"pull_request.merged_at": {"$ne": None}}},
    {"$group": {"_id": "$mentee", "merged": {"$sum": 1}}}
]

pipeline_total = [
    {"$group": {"_id": "$mentee", "total": {"$sum": 1}}}
]

# perform the aggregation
num_merged = Collection.aggregate(pipeline_merged)
num_total = Collection.aggregate(pipeline_total)

# print the results
for result in num_merged:
    print(result)
for result in num_total:
    print(result)
