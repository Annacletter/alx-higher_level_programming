#!/usr/bin/python3
def remove_char_at(str, n):
    anotherstr = ''
    if n >= 0:
        anotherstr += str[:n]
        anotherstr += str[n + 1:]
    else:
        anotherstr = str
    return anotherstr
