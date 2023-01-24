import requests, json, pymongo
from requests.auth import HTTPBasicAuth
from pymongo import MongoClient

# input info about project and run !! - make sure to change collection number too below
mentee_username  = "atrocitytheme"
mentor_usernames = ["sureshanaparti", "rohityadavcloud", "nvazquez"]
owner_name = "apache"
repo_name = "fineract-cn-mobile-wallet"

# database
myclient = MongoClient("mongodb+srv://HonourThesis:XZJXwB8NNdHIoxGw@cluster0.no1barz.mongodb.net/test")
db = myclient["GSoC21"]
Collection = db["17"]

def json_writer(name, json_object):
    with open(f"/Users/jasminemishra/Desktop/data/responses/{name}.json", "w") as outfile:
        outfile.write(json_object)
    name = name

def mongo_writer(file_data):
    print("HELLOOO")
    if isinstance(file_data, list):
        if(len(file_data) > 0):
            Collection.insert_many(file_data)
            print("many")
    else:
        Collection.insert_one(file_data)
        print("one")

# api AUTHENTICATION
username = 'coffeehousejazz'
token = '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'

### USER DATA ###
#api url to grab mentee user data
mentee_url = f"https://api.github.com/users/{mentee_username}"
# Writing mentee data to .json
#send get request
response = requests.get(mentee_url, auth=(username,token)).text
#save to object
data = json.loads(response)
json_serial = json.dumps(data, indent=4)
#json_writer("mentee", json_serial)
mongo_writer(data)
    
#api url to grab mentor user data
counter = 0
for name in mentor_usernames:
    counter = counter + 1
    mentor_url = f"https://api.github.com/users/{name}"
    #send get request
    response_m = requests.get(mentor_url, auth=(username,token)).text
    #save to object
    data_m = json.loads(response_m)
    json_serial_m = json.dumps(data_m, indent=4)
    #json_writer(f"mentor{counter}", json_serial_m)
    mongo_writer(data_m)

## MENTIONS ##
#api url to grab mentions
mentions_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues?mentions={mentee_username}&state=all"
#writing mentions to .json
#send get request
response2 = requests.get(mentions_url, auth=(username,token)).text
#save to object
data2 = json.loads(response2)
json_serial2 = json.dumps(data2, indent=4)
json_writer("mentions", json_serial2)
mongo_writer(data2)
    
## CREATOR ##
#api url to grab created
creator_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues?creator={mentee_username}&state=all"
# Writing created to .json
#send get request
response3 = requests.get(creator_url, auth=(username,token)).text
#save to object
data3 = json.loads(response3)
json_serial3 = json.dumps(data3, indent=4)
json_writer("creator", json_serial3)
mongo_writer(data3)

# read all the issue numbers into a list
issue_nums = []
for dic in data2:
    for key in dic:
        if key == "number":
            issue_nums.append(dic[key])

for dic in data3:
    for key in dic:
        if key == "number":
            issue_nums.append(dic[key])

for nums in issue_nums:
    print(nums)

# remove duplicates
issue_nums = list(dict.fromkeys(issue_nums))

# get all the comments data from issues into json files
for num in issue_nums:
    # issue number into api url
    #print(num)
    print("accessed")
    comments_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues/{num}/comments"
    #send get request
    response4 = requests.get(comments_url, auth=(username,token)).text
    #save to object
    data4 = json.loads(response4)
    print(data4)
    json_serial = json.dumps(data4, indent=4)
    #json_writer(f"{num}comments", json_serial)
    mongo_writer(data4)