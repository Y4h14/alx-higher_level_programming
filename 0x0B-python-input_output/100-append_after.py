#!/use/bin/python3
"""defines a fucntion"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    Args:
        - filename: the name of the file
        - search_string: the string to look for
        - new_string: the string to append
    """
    line_list = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(line_list)
