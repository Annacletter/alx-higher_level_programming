#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """prints list in ascending sort"""
        print(sorted(self))
