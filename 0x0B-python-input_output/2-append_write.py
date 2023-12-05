#!/usr/bin/python3


def append_write(filename="", text=""):
    """append text to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
