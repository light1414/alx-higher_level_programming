#!/usr/bin/python3
""" uses the URL and email to sends a POST request to the body of the response (decoded in utf-8) """

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    email_dict = {"email": email}
    email_encode = urllib.parse.urlencode(email_dict)
    email_encode = email_encode.encode('ascii')
    request = urllib.request.Request(url, email_encode)

    with urllib.request.urlopen(request) as response:
        pag = response.read()
        pag_decode = pag.decode('utf-8')
        print(pag_decode)
