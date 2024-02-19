#!/usr/bin/python3
"""It adds a new attr to an object
if it’s possible
"""


def add_attribute(obj, attribute, value):
    """it adds a new attr"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
