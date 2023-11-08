#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    result = 0
    total_weight = 0
    for score, weight in my_list:
        result += result * weight
        total_weight += weight

    return (result/total_weight)
