#!/usr/bin/python3
""" it sends a request to the URL and
prints the body of the response """

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            page = response.read().decode('utf-8')
            print(page)
    except urllib.request.HTTPError as e:
        print(f"Error code: {e.code}")
