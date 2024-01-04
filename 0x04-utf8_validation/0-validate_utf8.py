#!/usr/bin/python3
""" module to solve interview question """


def validUTF8(data):
    """ function check if data is utf8 or not """
    continuation_bytes = 0
    for byte in data:
        if byte < 0 or byte > 255:
            return False
        leading_ones = bin(byte)[2:].count('1')

        if leading_ones == 0:
            continuation_bytes = 0
            continue

        if continuation_bytes > 0:
            if leading_ones != 1:
                return False
            continuation_bytes -= 1
            continue

        if leading_ones > 4 or leading_ones == 1:
            return False

        continuation_bytes = leading_ones - 1

    return continuation_bytes == 0
