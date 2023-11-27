#!/usr/bin/python3
"""defines a function that divides a matrix"""


def matrix_divided(matrix, div):
    """
    divide a matrix to an int
    Args:
        -matix: a 2d matrix
        -div: a number to divide by 

    """
    result = []
    row_lenth = len(matrix[0])
    for i in matrix:
        for e in i:
            if type(e) is not int:
                if type(e) is not float:
                    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(i) != row_lenth:
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int:
        if type(div) is not float:
            raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    result = [[round(element / div, 2)for element in row]for row in matrix]

    return result

