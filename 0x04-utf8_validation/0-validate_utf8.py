#!/usr/bin/python3
"""
    Function that determines if a given dataset represents
    a valid UTF-8 encoding
"""


def validUTF8(data):
    """Return True if data is a valid utf-8 encoding"""
    new = [val > -128 and val <= 127 for val in data]
    if False in new:
        return False
    else:
        return True
