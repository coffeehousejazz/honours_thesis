import requests, json
from requests.auth import HTTPBasicAuth

def json_writer(name, json_object):
    with open(f"/Users/jasminemishra/Desktop/data/responses/{name}.json", "w") as outfile:
        outfile.write(json_object)

# AUTHENTICATION
username = 'coffeehousejazz'
token = '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'

## input info about project and run !!
mentee_username  = "theabhirath"
#mentor_usernames = ["", ""]
owner_name = "FluxML"
repo_name = "Metalhead.jl"

### USER DATA ###
#api url to grab mentee user data
mentee_url = f"https://api.github.com/users/{mentee_username}"
# Writing mentee data to .json
#send get request
response = requests.get(mentee_url, auth=(username,token))
#save to object
data = response.json()
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
json_serial = json.dumps(data2, indent=4)
json_writer("mentions", json_serial)
    
### CREATOR ###
#api url to grab created
creator_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues?creator={mentee_username}"
# Writing created to .json
#send get request
response3 = requests.get(creator_url, auth=(username,token)).text
#save to object
data3 = json.loads(response3)
json_serial = json.dumps(data3, indent=4)
json_writer("creator", json_serial)

# read all the issue numbers into a list
issue_nums = []
for v, k in data2.items():
    print(v)
    if v == "number":
       issue_nums.append(k)

for v, k in data3.items():
    print(v)
    if v == "number":
       issue_nums.append(k)
       
issue_nums = list(dict.fromkeys(issue_nums))

# get all the comments data into json files
for num in issue_nums:
   comments_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues/{num}/comments"
   #send get request
   response4 = requests.get(creator_url, auth=(username,token)).text
   #save to object
   data4 = json.loads(response4)
   json_serial = json.dumps(data4, indent=4)
   json_writer("creator", json_serial)