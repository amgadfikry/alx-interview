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
        print(' must be a number')
        exit(1)

    if chess_num < 4:
        print('N must be at least 4')
        exit(1)

    first_col = 1 if chess_num % 2 == 0 else 0
    end_col = chess_num - 1 if chess_num % 2 == 0 else chess_num
    incr = 2
    for i in range(first_col, end_col):
        result = []
        col = i
        result.append([0, i])
        for row in range(1, chess_num):
            col += incr
            if col >= chess_num and first_col == 1:
                col -= (chess_num + 1)
            if col >= chess_num and first_col == 0:
                col -= chess_num
            result.append([row, col])
        if first_col == 1:
            incr += 1
        print(result)


if __name__ == '__main__':
    nqueens()
