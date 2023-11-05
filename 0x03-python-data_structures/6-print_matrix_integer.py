#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for line in x:
            print("{:d}".format(line), end=" " if line != x[-1] else "")
        print()
