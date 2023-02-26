import requests, json
from requests.auth import HTTPBasicAuth

def json_writer(name, json_object):
    with open(f"/Users/jasminemishra/Desktop/data/responses/{name}.json", "w") as outfile:
        outfile.write(json_object)

# AUTHENTICATION
username = 'coffeehousejazz'
token = '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'

## input info about project and run !!
mentee_username  = "abheesht17"
mentor_usernames = ["", ""]
owner_name = "FluxML"
repo_name = "Metalhead.jl"

### USER DATA ###
#api url to grab mentee user data
mentee_url = f"https://api.github.com/users/{mentee_username}"
# Writing mentee data to .json
#send get request
response = requests.get(mentee_url, auth=(username,token)).text
#save to object
data = json.loads(response)
json_serial = json.dumps(data, indent=4)
json_writer("mentee", json_serial)
    
#api url to grab mentor user data
#for i in mentor_usernames:
#    mentor_url = f"https://api.github.com/users/{i}"
### . ###

### MENTIONS ###
#api url to grab mentions
mentions_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues?mentions={mentee_username}"
#writing mentions to .json
#send get request
response2 = requests.get(mentions_url, auth=(username,token)).text
#save to object
data2 = json.loads(response2)
json_serial2 = json.dumps(data2, indent=4)
json_writer("mentions", json_serial2)
    
### CREATOR ###
#api url to grab created
creator_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues?creator={mentee_username}"
# Writing created to .json
#send get request
response3 = requests.get(creator_url, auth=(username,token)).text
#save to object
data3 = json.loads(response3)
json_serial3 = json.dumps(data3, indent=4)
json_writer("creator", json_serial3)

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

# remove duplicates
issue_nums = list(dict.fromkeys(issue_nums))

# get all the comments data into json files
for num in issue_nums:
    # issue number into api url
   comments_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues/{num}/comments"
   #send get request
   response4 = requests.get(creator_url, auth=(username,token)).text
   #save to object
   data4 = json.loads(response4)
   json_serial = json.dumps(data4, indent=4)
   json_writer(f"{num}comments", json_serial)