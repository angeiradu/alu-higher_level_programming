#!/bin/bash
# cript that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sLw "%{http_code}" -o /dev/null "$1"
