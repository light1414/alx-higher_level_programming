#!/usr/bin/python3
"""The class MyList inherited from list
"""


class MyList(list):
    """The inherited from list"""
    def print_sorted(self):
        """It prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
