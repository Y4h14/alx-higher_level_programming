#!/usr/bin/python3
"""send a post request to the passed url with the email as parameter"""
from urllib import request, parse
import sys
if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    data = parse.urlencode(data).encode('utf-8')
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
