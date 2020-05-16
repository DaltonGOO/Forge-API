#You will need to setup Forge and add you app to BIM 360 before you can use this

#use this resource for getting all the parameters you need for your API REQUEST
#https://forge.autodesk.com/en/docs/bim360/v1/reference/http/projects-POST/



#import these packages
import requests
import json

#Authorization Token
url = "https://developer.api.autodesk.com/authentication/v1/authenticate"

# YOUR CLIENT ID GOES HERE
payload = ' '

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'PF=J0ofCWScdiNGKedchgGStv'
}

response = requests.request("POST", url, headers=headers, data = payload)

#token json
Token = (response.json())

#dumps the json object into an element
json_str = json.dumps(Token)

#load the json to a string
resp = json.loads(json_str)

#get the access_token for project
access_token = (resp["access_token"])

#combines Bearer and the access_token
TokenB = ('Bearer '+ access_token)

#POST the BIM 360 project | update the Accounts with your accounts id! That is the most important one
url = "https://developer.api.autodesk.com/hq/v1/accounts/YOURACCOUNTNUMBER/projects?name=TestProjectFromPythonthree&service_type=doc_manager&start_date=2020-05-01&end_date=2025-05-02&project_type=Commercial&value=100&currency=USD&job_number=50-0000"

# YOUR CLIENT ID GOED HERE
payload = ''

headers = {
  'Authorization': TokenB ,
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'PF=J0ofCWScdiNGKedchgGStv'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))










