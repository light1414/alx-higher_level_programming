#!/usr/bin/python3
"""
It module the sub class only
"""


def inherits_from(obj, a_class):
    """It returns True if the object is an instance of a class
       that inherited (directly or indirectly) from the specified class;
       else False.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
