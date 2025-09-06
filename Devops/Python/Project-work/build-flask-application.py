from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json


# Creating a flask app instance 

app = Flask(__name__)

##  Decarator in python , before you execute the function first it will execute the decarator action. it will start with @
# it performs the action before the execution of the function.
@app.route("/createJIRA", methods=["POST"])

def createJIRA():
    url = "https://nxk315.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("nxk315@gmail.com", "ATATT3xFfGF0IdyCOPo2ac4hr4gmEj2A4s6AlZibHFxKpwJ3sSpsWx8wnzOHMhLEdTOy-pyPaIRry9J5WHrTMz4PNzFD2cvKW0CCmFkttHUJ03p023nQaNNNwEeivaS_aLTvP6c573U5Zzlw9tHWSwCJOHSWz230znL3-FYueWGZP1VjW0qCUnw=ADCD0D09")

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My First Jira ticket created by Python script.",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10005"
        },
        "project": {
        "key": "KAN"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    

## flask will create a inbuilt server. it does not require tomcat to deploy 
## flask runs on port 5000 by default

app.run('0.0.0.0')