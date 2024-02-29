#!/bin/bash
# akes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | awk -F ': ' '{print $2}'
