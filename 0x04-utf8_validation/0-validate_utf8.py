#!/usr/bin/python3
"""
    Function that determines if a given dataset represents
    a valid UTF-8 encoding
"""


def validUTF8(data):
    """Return True if data is a valid utf-8 encoding"""
    expected_continuation_bytes = 0

    # Iterate through the list of integers
    for byte in data:
        # Convert the byte to an 8-bit binary string
        binary_byte = format(byte, '08b')

        # If we are not expecting continuation bytes, check the prefix
        if expected_continuation_bytes == 0:
            if binary_byte[0] == '0':
                # This is a single-byte character
                continue
            elif binary_byte[:3] == '110':
                # This is the start of a 2-byte character
                expected_continuation_bytes = 1
            elif binary_byte[:4] == '1110':
                # This is the start of a 3-byte character
                expected_continuation_bytes = 2
            elif binary_byte[:5] == '11110':
                # This is the start of a 4-byte character
                expected_continuation_bytes = 3
            else:
                # Invalid prefix
                return False
        else:
            # If this byte is a continuation byte (starts with '10')
            if binary_byte[:2] == '10':
                expected_continuation_bytes -= 1
            else:
                # Invalid continuation byte
                return False

    return expected_continuation_bytes == 0
