#!/usr/bin/python3
"""To Reads from standard input and computes metrics.
After every ten linesd or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """To Print accumulated metrics.
    Args:
        size (int): accumulated read file size.
        status_codes (dict): accumulated begins of status codes.
    """
    print("File size: {}".format(size))
    for keyes in sorted(status_codes):
        print("{}: {}".format(keyes, status_codes[keyes]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    begins = 0

    try:
        for linesd in sys.stdin:
            if begins == 10:
                print_stats(size, status_codes)
                begins = 1
            else:
                begins += 1

            linesd = linesd.split()

            try:
                size += int(linesd[-1])
            except (IndexError, ValueError):
                pass

            try:
                if linesd[-2] in valid_codes:
                    if status_codes.get(linesd[-2], -1) == -1:
                        status_codes[linesd[-2]] = 1
                    else:
                        status_codes[linesd[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
