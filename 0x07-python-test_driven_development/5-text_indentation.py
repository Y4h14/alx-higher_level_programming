#!/usr/bin/python3
"""define an indentation function"""


def text_indentation(text):
    """
    Args:
        -text (str): a string
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in text:
        if i in ['?', ':', '.']:
            print("{}\n".format(i))
        else:
            print(i, end='')
