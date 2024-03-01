#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys
"""sends a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter"""
if __name__ == "__main__":
    if sys.argv[1]:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    res = requests.post(url, data=payload)

    try:
        json_data = res.json()

        if isinstance(json_data, dict) and not json_data:
            print("No result")
        else:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")

    except Exception:
        print("Not a valid JSON")
