#!/usr/bin/python3
"""The Rectangle Class"""


class Rectangle:
    """The class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """It initializes both height and width to zero"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Puts the width"""
        return self.__width

    @property
    def height(self):
        """Put the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Puts the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
    Cal the area of the rectangle
    """
    def area(self):
        return (self.__width * self.__height)

    """
    Cal the perimeter of the rectangle
    """
    def perimeter(self):
        if not self.area():
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """It returns a printable object"""
        if not self.area():
            return ""
        for i in range(self.__height - 1):
            print(f"{str(self.print_symbol) * self.__width}")
        print(f"{str(self.print_symbol) * self.__width}", end="")
        return ""

    def __repr__(self):
        """It returns the string representation of the rectangle"""
        string = "Rectangle(" + str(self.__width) + ", "
        string += str(self.__height) + ")"
        return (string)

    def __del__(self):
        """It deletes an instance of the rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A static method to compare sizes of two rectangles"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_diff = rect_2.area() - rect_1.area()
        if area_diff > 0:
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """New Rectangle instance with width == height == size"""
        return cls(size, size)
