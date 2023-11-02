#!/usr/bin/python3
if __name__ == "__main__":
    """print the sum of arguments"""
from sys import argv
result = 0
for i in range(1, len(argv)):
    result += int(argv[i])
print(result)
