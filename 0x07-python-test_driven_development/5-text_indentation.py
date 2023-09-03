#!/usr/bin/python3
"""
Text Indentation Module

This module prints a text with 2 new lines after '.', '?', and ':' characters.
"""

def text_indentation(text):
    """
    Print a text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("This is a sample text. It has some sentences: like this one? And another one.")
        This is a sample text.
        It has some sentences:
        like this one?
        And another one.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
