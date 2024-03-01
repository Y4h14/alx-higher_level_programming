#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv

if __name__ == "__main__":
    q = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        r_dict = r.json()
        Id, name = r_dict.get('id'), r_dict.get('name')
        if len(r_dict) == 0 or not Id or not name:
            print("No result")
        else:
            print("[{}] {}".format(Id, name)
    except Exception as e:
        print("Not a valid JSON")
