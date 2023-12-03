#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()

    for num in my_list:
        unique_set.add(num)
        
    result_sum = sum(unique_set)
    return result_sum
