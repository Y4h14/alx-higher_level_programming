#!/bin/bash
# akes in a URL and displays all HTTP methods the server will accept
curl -sX OPTIONS "$1" 
