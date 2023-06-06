#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return (list(map(lambda b: replace if b is search else b, my_list)))
