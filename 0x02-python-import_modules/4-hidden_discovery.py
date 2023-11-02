#!/usr/bin/python3
if __name__ == "__main__":
    """print names defined in the module"""
import hidden_4
module_naime = dir(hidden_4)
for module in module_name:
    if module[:2] != "__":
        print(module)
