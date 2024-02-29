#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sH "Content-Type: application/json" "$1" -d "$(cat "$2")"
