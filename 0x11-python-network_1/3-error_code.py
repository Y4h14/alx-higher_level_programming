#!/usr/bin/python3
"""sends a request and catches errors"""
from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
