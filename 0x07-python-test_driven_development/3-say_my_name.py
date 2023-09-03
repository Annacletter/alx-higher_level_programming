#!/usr/bin/python3
"""
Say My Name Module

This module prints a full name or raises a TypeError exception with custom error messages.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a full name using the given first and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {:s} {:s}".format(first_name, last_name))
