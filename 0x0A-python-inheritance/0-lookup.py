#!/usr/bin/python3
"""Object attribute lookup function."""


def lookup(obj):
    """Return list of an object's available attributes."""
    return dir(obj)
