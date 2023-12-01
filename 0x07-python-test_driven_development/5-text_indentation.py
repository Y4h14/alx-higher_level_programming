#!/usr/bin/python3
"""define an indentation function"""


def text_indentation(text):
    """
    Args:
        -text (str): a string
    """
    string = ""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for ch in text:
        string += ch
        if ch in ['?', ':', '.']:
            string += "\n\n"
        else:
            print(string, end='')
