#!/usr/bin/python3
""" module to solve interview question """


def validUTF8(data):
    """ function check if data is utf8 or not """
    continous = 0
    for i in range(len(data)):
        if data[i] < 0 or data[i] > 255:
            return False
        if continous > 0:
            continous -= 1
            num_bin = '{0:08b}'.format(data[i])
            char_long = num_bin.find('0')
            if char_long != 1:
                return False
            continue
        if data[i] > 127 and data[i] < 256:
            num_bin = '{0:08b}'.format(data[i])
            char_long = num_bin.find('0')
            if char_long > 4 or char_long < 2:
                return False
            continous += char_long
    return True
