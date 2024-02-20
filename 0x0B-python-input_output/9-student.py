#!/usr/bin/python3

"""It defines the class Student."""


class Student:
    """It rep a student."""

    def __init__(self, first_name, last_name, age):
        """Starts a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary rep of the Student."""
        return self.
