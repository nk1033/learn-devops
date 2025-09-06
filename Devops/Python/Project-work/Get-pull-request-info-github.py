import requests

response = requests.get("https://api.github.com/repos/nk1033/python-for-devops/pulls")
complete_details = response.json()

def get_pull_request():

    for i in range(len(complete_details)):
        print(complete_details[0]["url"])
        print("Pull request created by", complete_details[i]["user"]["login"] )

def message():
    print("This is test function...")

get_pull_request()

