#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is None:
            # If attrs is not provided, return all attributes
            return self.__dict__

        if not isinstance(attrs, list):
            raise ValueError("attrs should be a list of attribute names")

        result = {}
        for attr in attrs:
            if not isinstance(attr, str):
                raise ValueError("Attribute names in attrs should be strings")
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)

        return result

