#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for l in x :
            print("{}".format(l), end="")
        print()
