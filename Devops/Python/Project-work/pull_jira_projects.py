# Create a Jira if the request from github is /jira.. we should create a web hook token and send request to python and from python we need to call Jira API to create jira ticket.

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nxk315.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("nxk315@gmail.com", "ATATT3xFfGF0IdyCOPo2ac4hr4gmEj2A4s6AlZibHFxKpwJ3sSpsWx8wnzOHMhLEdTOy-pyPaIRry9J5WHrTMz4PNzFD2cvKW0CCmFkttHUJ03p023nQaNNNwEeivaS_aLTvP6c573U5Zzlw9tHWSwCJOHSWz230znL3-FYueWGZP1VjW0qCUnw=ADCD0D09")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# we need to convert from json to dictionary.
complete_output = json.loads(response.text)

name = complete_output[0]["name"]

print(name)