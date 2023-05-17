#!/usr/bin/python3
def search_replace(my_list, search, replace):
    curren_lists = list(map(lambda x: replace if x == search else x, my_list))
    return (curren_lists)
