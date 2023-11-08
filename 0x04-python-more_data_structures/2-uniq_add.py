#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = []
    result = 0
    for i in my_list:
        if i in temp:
            continue
        temp.append(i)
    for i in range(0, len(temp)):
        result += temp[i]
    return (result)
