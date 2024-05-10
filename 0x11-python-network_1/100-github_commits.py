#!/usr/bin/python3
"""Displays 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository owner> <repository name>
"""
import sys
import requests
import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        syst.argv[2], syst.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
