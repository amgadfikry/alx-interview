#!/usr/bin/python3
""" module to solve interview question """


def validUTF8(data):
    """ function check if data is utf8 or not """
    continous = 0
    for num in data:
        if num < 0 or num > 255:
            return False
        num_bin = '{0:08b}'.format(num)
        char_long = num_bin.find('0')
        if continous > 0:
            continous -= 1
            if char_long != 1:
                return False
            continue
        if char_long > 3:
            return False
        continous = char_long - 1 if char_long > 0 else 0
    return continous == 0
