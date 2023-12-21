#!/usr/bin/python3
"""solve interview question of parselog metrics"""
import fileinput
from ipaddress import ip_address
from datetime import datetime


def check_line(line):
    """function check line is same pattern
        Args:
            line (str): line of log file
        Returns:
            bool: True if line is same pattern, False otherwise
    """
    arr = line.split(' ')
    if len(arr) != 9:
        return False
    try:
        ip_address(line.split(' ')[0])
    except ValueError:
        return False
    if line.split(' ')[1] != '-':
        return False
    date_fromat = '%Y-%m-%d %H:%M:%S.%f'
    if not datetime.strptime(line.split('[')[1].split(']')[0], date_fromat):
        return False
    if line.split('"')[1] != 'GET /projects/260 HTTP/1.1':
        return False
    try:
        x = int(arr[7])
        y = int(arr[8])
    except ValueError:
        return False
    return True


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
            if not check_line(line):
                continue
            line_num += 1
            state_code = line.split(' ')[7]
            total_size += int(line.split(' ')[8])
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
