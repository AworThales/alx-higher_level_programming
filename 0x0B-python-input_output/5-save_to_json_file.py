#!/usr/bin/python3
"""A JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to the text file using JSON representation."""
    with open(filename, "w") as ft:
        json.dump(my_obj, ft)
