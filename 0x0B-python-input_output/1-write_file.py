#!/usr/bin/python3

"""It defines a file-writing function."""


def write_file(filename="", text=""):
    """It write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The numb of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
