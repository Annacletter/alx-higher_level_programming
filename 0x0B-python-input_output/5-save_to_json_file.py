#!/usr/bin/python3
"""Write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to text file, using JSON rep"""

    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
