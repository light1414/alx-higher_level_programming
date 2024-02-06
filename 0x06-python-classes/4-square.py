#!/usr/bin/python3
""" Forming a class Square"""


class Square:
    """Square object of a class"""

    def __init__(self, size=0):
        """Starts the instances of a classs"""
        self.size = size

    @property
    def size(self):
        """Gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """gets the __size to value"""
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Prints the area of the square"""
        return (self.__size ** 2)
