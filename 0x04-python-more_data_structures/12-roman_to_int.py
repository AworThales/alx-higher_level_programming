#!/usr/bin/python3
def to_subtract(list_num):
    to_subs = 0
    max_record = max(list_num)

    for n in list_num:
        if max_record > n:
            to_subs += n

    return (max_record - to_subs)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_numbs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_numbs.keys())

    nums = 0
    end_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_numbs.get(ch) <= end_rom:
                    nums += to_subtract(list_num)
                    list_num = [rom_numbs.get(ch)]
                else:
                    list_num.append(rom_numbs.get(ch))

                end_rom = rom_numbs.get(ch)

    nums += to_subtract(list_num)

    return (nums)
