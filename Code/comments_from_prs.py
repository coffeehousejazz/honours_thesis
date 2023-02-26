import requests, json
from pymongo import MongoClient
## this code gets the comments from pull requests
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
src_col = db["Pulls"]
dst_col = db["Comments"]

# API AUTHENTICATION
me_user = 'coffeehousejazz'
token = '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'

# writes json files - to mongo
def mongo_writer(file_data):
    # for many files
    if isinstance(file_data, list):
        if(len(file_data) > 0):
            dst_col.insert_many(file_data)
            print("many")
    # for one file
    else:
        dst_col.insert_one(file_data)
        print("one")

cursor = src_col.find()

# Iterate over the cursor and print each document
for document in cursor:
    print(document)

# grab comments from prs (same)
#for num in issue_nums:
#    # issue number into api url
#    print("accessed")
#    comments_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues/{num}/comments"
#    #send get request
#    response4 = requests.get(comments_url, auth=(username,token)).text
#    #save to object
#    data4 = json.loads(response4)
#    print(data4)
#    json_serial = json.dumps(data4, indent=4)
#    mongo_writer(data4)