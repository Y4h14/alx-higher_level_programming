#!/usr/bin/python3
"""defines a function that reads a file and print it's content"""


def read_file(filename=""):
    """reads contents of a file and print them"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
