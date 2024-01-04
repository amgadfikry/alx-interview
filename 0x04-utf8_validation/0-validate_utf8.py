#!/usr/bin/python3
""" module to solve interview question """


def validUTF8(data):
    """ function check if data is utf8 or not """
    for i in range(len(data)):
        if data[i] < 0 or data[i] > 255:
            return False
        if data[i] > 127 and data[i] < 256:
            num_bin = '{0:08b}'.format(data[i])
            char_long = num_bin.find('0')
            if char_long > 4 or char_long == -1:
                return False
            for j in range(i + 1, char_long):
                cont_byte = '{0:08b}'.format(data[j])
                if cont_byte.find('0') != 1:
                    return False
            i = i + int(char_long) - 1
        if i >= len(data):
            return False
    return True
