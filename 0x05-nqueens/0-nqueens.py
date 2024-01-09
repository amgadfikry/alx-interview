#!/usr/bin/python3
""" module to solve interview problem """
from sys import argv


def nqueens():
    """ solve problem of n queens interview problem """
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    chess_num = argv[1]

    try:
        chess_num = int(chess_num)
    except ValueError:
        print('N must be a number')
        exit(1)

    if chess_num < 4:
        print('N must be at least 4')
        exit(1)

    incr = 2
    for i in range(1, chess_num - 1):
        result = []
        col = i
        result.append([0, i])
        for row in range(1, chess_num):
            col += incr
            if col >= chess_num:
                col -= (chess_num + 1)
            result.append([row, col])
        incr += 1
        print(result)


if __name__ == '__main__':
    nqueens()
