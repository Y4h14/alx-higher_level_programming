#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if ord(c) in range(97, 123):
            upper = ord(c) - 32
            result += chr(upper) 
        else:
            result += c
    print("{}".format(result))
