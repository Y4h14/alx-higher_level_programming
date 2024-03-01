#!/usr/bin/python3
"""takes GitHub credentials (username and password) and uses the
GitHub API to display ID"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    token = argv[2]
    url = "https://api.github.com/user"
    res = requests.get(url, auth=HTTPBasicAuth(user, token))
    try:
        user_id = res.json()['id']
    except KeyError:
        user_id = None
    print(user_id)
