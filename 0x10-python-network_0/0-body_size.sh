#!/bin/bash
# Send a request to a URL and access the body size
curl -s -I "$1" | grep 'Content-Length'
