1.
#!/usr/bin/python3
"""Adding two integers"""


def add_integer(a, b=98):
    """Two numbers to add
    args:
    a - int or float
    b - or integer whose base value is 98
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

2.

#!/usr/bin/python3
"""It Defines a matrix by int or float"""


def matrix_divided(matrix, div):
    """It Divs all the element of a matrix by int/float div
    args:
        matrix: Matrix where every element is either float or int
        div (int or float): div all matrix elements
        """

    if type(div) not in [int, float]:
        raise TypeError("the div must be a numb")
    if div == 0:
        raise ZeroDivisionError("div by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("each row of the matrix must have the same size")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        text = "the matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(text)

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
