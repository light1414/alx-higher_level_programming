#!/usr/bin/python3
"""
to write a class Square that inherits from Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    The Square class shape, inheirts from BaseGeometry
    """
    def __init__(self, size):
        """"
        The init function for Square

        Attributes:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion to print with/height

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        The function that cal the area of the Square
        """
        return self.__size ** 2
