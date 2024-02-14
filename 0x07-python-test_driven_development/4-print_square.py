#!/usr/bin/python3
"""It Prnts the full name"""


def say_my_name(first_name, last_name=""):
    """Only the string of last name and first name are accapted"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


4. 4-print_square.py

#!/usr/bin/python3
"""
This shows a square-printing function.
"""


def print_square(size):
    """ This Function prints the square with the char #
    Args:
        size: the size of the square printed
    Returns:
        No return
    Raises:
        TypeError: If the size is not integer numb
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
