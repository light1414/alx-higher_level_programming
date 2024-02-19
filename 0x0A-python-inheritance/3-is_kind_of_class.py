#!/usr/bin/python3
"""It module check class answer subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Prints True if the object is an instance of, or if the object
    is an instance
    of a class that inherited from, the specified class ; else False
    """
    return isinstance(obj, a_class)
