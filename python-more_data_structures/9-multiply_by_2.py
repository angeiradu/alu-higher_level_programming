#!/usr/bin/python3
def multiply_by_2(my_dict):
    tmp_dict = my_dict.copy()
    for s in tmp_dict.keys():
        tmp_dict[s] *= 2
    return (tmp_dict)
