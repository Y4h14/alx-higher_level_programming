#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            result.append(replace)
        else:
            result.append(my_list[i])
    return (result)
