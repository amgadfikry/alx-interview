#!/usr/bin/python3
""" module to solve interview question """


def validUTF8(data):
    """ function check if data is utf8 or not """
    continous_bytes = 0

    for byte in data:
        byte_bin = '{0:08b}'.format(byte)[-8:]
        leading_ones = byte_bin.find('0')

        if continous_bytes > 0:
            if leading_ones != 1:
                return False
            continous_bytes -= 1
            continue

        if leading_ones == 0:
            continue

        if leading_ones > 4 or leading_ones == 1:
            return False

        continous_bytes = leading_ones - 1

    return continous_bytes == 0
