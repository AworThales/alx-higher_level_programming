#!/usr/bin/python3
"""A JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create Python object from a JSON file."""
    with open(filename) as ft:
        return json.load(ft)
