#!/usr/bin/python3
"""Gets header with requests module
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    re = requests.get(url)
    re = re.headers
    print(re.get('X-Request-Id'))
