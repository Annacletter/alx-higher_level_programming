#!/usr/bin/python3

def add_integer(a, b=98):
    """Function that adds 2 integers and returns an int
       Args: a and b
         If not integers or floats raise TypeError
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both a and b must be integers or floats")
    
    return int(a) + int(b)
