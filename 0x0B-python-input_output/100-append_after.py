#!/usr/bin/python3
"""A texts file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert texts after each lines containing a given string in a file.
    Args:
        filename (str): A name of the file.
        search_string (str): A string to search for within the file.
        new_string (str): The string to insert.
    """
    texts = ""
    with open(filename) as s:
        for lines in s:
            texts += lines
            if search_string in lines:
                texts += new_string
    with open(filename, "w") as ft:
        ft.write(texts)
