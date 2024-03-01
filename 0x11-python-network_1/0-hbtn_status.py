#!/usr/bin/python3
"""fetches data from a website"""
from urllib import request
if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        res = response.read()
    print('Body Response')
    print(f"\t - type: {type(res)}")
    print(f"\t - content: {res}")
    print(f"\t - utf8 content: {res.decode('utf-8')}")
