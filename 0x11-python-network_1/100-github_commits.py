#!/usr/bin/python3
"""list 10 commits of the repository 'rails'"""
from sys import argv
import requests


repo = argv[1]
owner = argv[2]
url = f"https://api.github.com/repos/{owner}/{repo}/commits"
headers = {'Accept': 'application/vnd.github+json',
           'X-GitHub-Api-Version': '2022-11-28'}
res = requests.get(url, headers=headers)
try:
    commits = res.json()[:10]
except Exception:
    user_id = None
for commit in commits:
    print(f"{commit['sha']}: {commit['commit']['author']['name']}")
