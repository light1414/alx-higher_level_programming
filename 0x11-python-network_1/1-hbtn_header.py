#!/usr/bin/python3
"""  Sends a request to the URL and displays the value."""

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        unique_id = response.headers.get("X-Request-Id")
        print(header)
