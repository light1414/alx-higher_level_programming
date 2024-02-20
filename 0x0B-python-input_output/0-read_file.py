#!/usr/bin/python3

"""The module containing functions that reads from a file ."""


def read_file(filename=""):
    """It print the contents of a UTF8 text file to stdout."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
