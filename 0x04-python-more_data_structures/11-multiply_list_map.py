#!/usr/bin/python3

from typing import List

def multiply_list_map(my_list: List[int] = None, number: int = 0) -> List[int]:
    if my_list is None:
        my_list = []
    return list(map(lambda x: x * number, my_list))
