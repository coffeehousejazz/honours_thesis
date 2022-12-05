import requests, json

def json_responses(url):
    #send get request
    response = requests.get(url)
    #save to object
    data = response.json()
    # Serializing json
    return json.dumps(data, indent=4)

def json_writer(name, json_object):
    with open(f"/Users/jasminemishra/Desktop/{name}.json", "w") as outfile:
        outfile.write(json_object)

## input info about project and run !!
mentee_username  = "theabhirath"
#mentor_usernames = ["", ""]
owner_name = "FluxML"
repo_name = "Metalhead.jl"

### USER DATA ###
#api url to grab mentee user data
mentee_url = f"https://api.github.com/users/{mentee_username}"
# Writing mentee data to .json
json_object = json_responses(mentee_url)
json_writer("mentee", json_object)
    
#api url to grab mentor user data
#for i in mentor_usernames:
#    mentor_url = f"https://api.github.com/users/{i}"

### . ###

### MENTIONS ###
#api url to grab mentions
issue_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues?mentions={mentee_username}"
# Writing mentions to .json
json_object = json_responses(issue_url)
json_writer("mentions", json_object)
    
### CREATOR ###
#api url to grab created
creator_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues?creator={mentee_username}"
# Writing created to .json
json_object = json_responses(issue_url)
json_writer("creator", json_object)
    
# read all the issue numbers into a list
issue_nums = []

issue_nums.append()

# get all the comments data into json files
for num in issue_nums:
    comments_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues/{num}/comments"
    json_object = json_responses(comments_url)
    with open(f"/Users/jasminemishra/Desktop/{num}comments.json", "w") as outfile:
        outfile.write(json_object)