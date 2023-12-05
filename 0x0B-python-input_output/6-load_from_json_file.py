#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """create an object form JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.loads(f.read()))
