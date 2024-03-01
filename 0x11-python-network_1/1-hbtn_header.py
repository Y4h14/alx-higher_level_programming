#!/usr/bin/python3
"""display the value of X-Request-Id from a url response"""
from urllib import request
import sys
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
