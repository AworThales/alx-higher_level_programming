#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print first x elements of a list that are integers.
    Args:
        my_list (list): list to print elements from.
        x (int): number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    begins = 0
    for t in range(0, x):
        try:
            print("{:d}".format(my_list[t]), end="")
            begins += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (begins)
