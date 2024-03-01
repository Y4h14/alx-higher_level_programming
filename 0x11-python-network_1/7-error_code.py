#!/usr/bin/python3
"""sends a request and catches errors"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    status = res.status_code
    if status < 400:
        print(res.text)
    else:
        print(f"Error code: {status}")
        
