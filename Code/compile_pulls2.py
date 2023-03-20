import requests, json, time
from pymongo import MongoClient
# this code puts the pulls from users in the db
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC"]
src_col = db["Users"]
dst_col = db["PullsREAL"]
# db redesign

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

# get usernames and repo names
cur = src_col.find({"mentee": True}, {"login": 1, "owner_name": 1, "repo_name" : 1})
counter = 0
for x in cur:
    for key in x:
        if key == "login":
            username = x[key]
        if key == "owner_name":
            owner_name = x[key]
        if key == "repo_name":
            repo_name = x[key]
    # grab prs (new)
    pr_url = f"https://api.github.com/search/issues?q=type:pr+repo:{owner_name}/{repo_name}+involves:{username}"
    # send get request
    response2 = requests.get(pr_url, auth=(me_user,token)).text
    response1 = requests.get(pr_url, auth=(me_user,token))
    
    while response1.status_code == 403:
        print('Error:', response1.status_code, response1.text)
        time.sleep(60)
        print("waiting 60 seconds")
        response2 = requests.get(pr_url, auth=(me_user,token)).text
        response1 = requests.get(pr_url, auth=(me_user,token))
        print("reached 11111111")
    print("reached 222222222")
    if response1.status_code == 200:
        items = json.loads(response2)['items']
        print(type(items))
        for pr in items:
            counter+=1
            pr['mentee_name'] = username
            pr['owner_name'] = owner_name
            pr['repo_name'] = repo_name
            # add the username of the mentee to the pull so that we can identify who is mentioned
            pr_json = json.dumps(pr, indent=4)
            #########################################################
            #### UNCOMMENT BELOW COMMENT WHEN READY to add to db ####
            #########################################################
            print(counter)
            mongo_writer(pr)

print("finished")
# save to object
    ###### data2 = json.loads(response2)
    ###### mongo_writer(data2)
# get numbers from prs

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