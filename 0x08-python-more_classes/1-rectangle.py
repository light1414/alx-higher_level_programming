#!/usr/bin/python3
"""

A class that defines a Rectangle makes up this module.


"""


class Rectangle:
    """ class that describes a rectangle """

    def __init__(self, width=0, height=0):
        """ The procedure for initializing the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle


        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ technique that yields the width value

        Returns:
            width of the rectangle


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ The method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ technique that yields the height's value

        Returns:
            height of the rectangle


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ technique that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
