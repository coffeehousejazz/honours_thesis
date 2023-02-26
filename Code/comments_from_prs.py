import requests, json
from pymongo import MongoClient
## this code gets the comments from pull requests
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
src_col = db["Pulls2"]
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

# Get a cursor to the documents in the collection
cursor = src_col.find()
# Iterate over the cursor and print each document in the Pulls2 collection
for document in cursor:
    print(document)
    # get PR/issue number for document
    pr_num = document["number"]
    # get mentee username for document
    mentee_name = document["mentee"]
    # get owner name for document
    owner_name = document["owner_name"]
    # get repo name for document
    repo_name = document["repo_name"]
    # comments_url
    comments_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues/{pr_num}/comments"
    response1 = requests.get(comments_url, auth=(me_user,token))
    response2 = requests.get(comments_url, auth=(me_user,token)).text
    # add mentee username, ownername, reponame
    if response1.status_code == 200:
        data = json.loads(response2)
        # check data types
        print(type(data))
        # if list, add, if not list add differently
        # add mentee username, ownername, reponame
    # write to mongo

# grab comments from prs
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