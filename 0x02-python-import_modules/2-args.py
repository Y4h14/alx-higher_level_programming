#!/usr/bin/python3
if __name__ == "__main__":
    """print the number of arguments and their values"""
from sys import argv
if len(argv) == 1:
    print("0 arguments.")
elif len(argv == 2):
    print("1 arguement:")
else:
    print("{} arguments:".format(len(argv) - 1))
for i in range(1, len(argv)):
    print("{}: {}".format(i, argv[i]))
