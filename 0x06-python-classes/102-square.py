#!/usr/bin/python3
"""Assigns a class Square."""


class Square:
    """Rep a square."""

    def __init__(self, size=0):
        """Starts a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the real area of the square."""
        return (self.__size ** 2)

    def __eq__(self, other):
        """States the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """States the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """States the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """States the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """States the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """States the >= compmarison to a Square."""
        return self.area() >= other.area()
