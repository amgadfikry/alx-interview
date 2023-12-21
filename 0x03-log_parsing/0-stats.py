#!/usr/bin/python3
"""solve interview question of parselog metrics"""
import fileinput
from ipaddress import ip_address
from datetime import datetime


def print_me(size, status):
    """print final results of status code
        Args:
            size (int): total size of file
            status (Dict[str, int]): status code and count
        Returns:
            None
    """
    print('File size: {}'.format(size))
    keys = sorted([k for k in status])
    for k in keys:
        print('{}: {}'.format(k, status[k]))


def main():
    """main function entry point
        Args:
            None
        Returns:
            None
    """
    status = {}
    total_size = 0
    line_num = 0
    try:
        for line in fileinput.input():
            line = line.rstrip()
            line_num += 1
            state_code = line.split(' ')[-2]
            total_size += int(line.split(' ')[-1])
            if state_code in status:
                status[state_code] += 1
            else:
                status[state_code] = 1
            if line_num % 10 == 0:
                print_me(total_size, status)
    except KeyboardInterrupt:
        print_me(total_size, status)
    finally:
        print_me(total_size, status)


if __name__ == '__main__':
    main()
