#!/usr/bin/python3

"""It defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """It returns the JSON rep of a string object."""
    return json.dumps(my_obj)
