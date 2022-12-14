import requests, json
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["key", "value"]

github_username  = "khatrivinay1"

#api url to grab public user data
api_url = f"https://api.github.com/users/{github_username}"

#send get request

response = requests.get(api_url)

#get json data in object
data = response.json()

# Serializing json
json_object = json.dumps(data, indent=4)
 
# Writing to .json
with open("/Users/jasminemishra/Desktop/mentor.json", "w") as outfile:
    outfile.write(json_object)