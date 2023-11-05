#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for ch in my_string:
        if ord(ch) != ord('c'):
            if ord(ch) != ord('C'):
                new_str += ch
    return (new_str)
