#!/bin/bash
# Send a request to a URL and access the body size

curl -I "$1" | grep 'Content-Length'
