#!/usr/bin/python3
"""sends a request and catches errors"""
import requests
import sys

if __name__ == "__main__":
    try:
        res = requests.get(sys.argv[1])
        print(res.text)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
