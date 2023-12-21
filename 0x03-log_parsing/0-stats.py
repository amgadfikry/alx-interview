#!/usr/bin/python3
"""solve interview question """
import fileinput
from ipaddress import ip_address
from datetime import datetime
from typing import List, Dict


def check_line(line: str) -> bool:
    """function check line is same pattern"""
    arr: List[str] = line.split(' ')
    if len(arr) != 9:
        return False
    try:
        ip_address(line.split(' ')[0])
    except ValueError:
        return False
    if line.split(' ')[1] != '-':
        return False
    date_fromat: str = '%Y-%m-%d %H:%M:%S.%f'
    if not datetime.strptime(line.split('[')[1].split(']')[0], date_fromat):
        return False
    if line.split('"')[1] != 'GET /projects/260 HTTP/1.1':
        return False
    try:
        int(arr[7])
        int(arr[8])
    except ValueError:
        return False
    return True


def print_me(size: int, status: Dict[str, int]):
    """print final results of status code"""
    print('File size: {}'.format(size))
    keys: List[str] = sorted([k for k in status])
    for k in keys:
        print('{}: {}'.format(k, status[k]))


def main() -> None:
    """main function entry point"""
    status: Dict[str, int] = {}
    total_size: int = 0
    line_num: int = 0
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


if __name__ == '__main__':
    main()
