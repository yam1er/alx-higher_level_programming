#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cunt = 0
    for element in my_list:
        try:
            print("{:d}".format(element))
            count += 1
        except (ValueError, TypeError):
            pass
        if count == x:
            break
    return count
