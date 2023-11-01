#!/usr/bin/python3
def remove_char(srt, n):
    if n > 0 and n < len(str):
        return str[:n] + str[n + 1:]
