#!/usr/bin/python3
""" module that form pascal function """


def pascal_triangle(n):
    """ function hat returns a list of lists of integers
      representing the Pascal’s triangle of n
      Params:
      n: number of items in pascal triangle
      Return:
      list of list of integers or empty list
    """
    res = []
    for i in range(n):
        if i == 0:
            res.append([1])
        else:
            li = res[i - 1]
            newli = [1]
            for index, num in enumerate(li):
                if index + 1 < len(li):
                    newli.append(num + li[index + 1])
                else:
                    newli.append(1)
                    res.append(newli)
    return res
