#!/usr/bin/python3
def to_subtract(list_num):
    to_subtr = 0
    max_record = max(list_num)

    for t in list_num:
        if max_record > t:
            to_subtr += t

    return (max_record - to_subtr)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numbs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_numbs.keys())

    numb = 0
    end_roms = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if roman_numbs.get(ch) <= end_roms:
                    numb += to_subtract(list_num)
                    list_num = [roman_numbs.get(ch)]
                else:
                    list_num.append(roman_numbs.get(ch))

                end_roms = roman_numbs.get(ch)

    numb += to_subtract(list_num)

    return (numb)
