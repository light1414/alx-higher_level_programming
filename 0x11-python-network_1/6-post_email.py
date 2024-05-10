#!/usr/bin/python3
"""A script that make a post request."""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    r = requests.post(url, data=val)
    print(r.text)
