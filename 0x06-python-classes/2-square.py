#!/usr/bin/python3
""" Forming a class Square"""


class Square:
    """Square object of a class"""

    def __init__(self, size=0):
        """starts the instances of the class"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
