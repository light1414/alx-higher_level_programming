#!/usr/bin/python3

"""
This python script fetch web response
"""

import urllib.request


def fetch_url(url):
    """
    This fetches the contents of the URL
    """
    with urllib.request.urlopen(url) as response:
        return response.read()


def display_info(response):
    """
    Print the information about HTTP response.
    Args:
        response: Bytes object rep the body of the HTTP response.
    """
    body = response.decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(body))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response_body = fetch_url(url)
    display_info(response_body)
