#!/usr/bin/env bash
# Takes in a URL, sends a request to that URL, and displays
# the size of the body of the response

curl -sw ' %{size_download}' "$1" | cut -d ' ' -f3
