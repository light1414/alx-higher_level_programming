#!/usr/bin/python3
"""Adding two integers"""


def add_integer(a, b=98):
    """Two numbers to add
    args:
    a - int or float
    b - or integer whose base value is 98
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
