#!/usr/bin/python3
"""takes GitHub credentials (username and password) and uses the
GitHub API to display ID"""
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    token = argv[2]
    url = "https://api.github.com/user"
    headers = {"Authorization": f"Bearer {token}",
               "X-GitHub-Api-Version": "2022-11-28"}
    res = requests.get(url, headers=headers)
    if len(res.json()) != 0:
        print(res.json()['id'])
    else:
        print(None)
