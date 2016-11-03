import os
import sys
import re


def illegal_length(name, max_length=250):
    if len(name) > max_length:
        return True


def illegal_characters(name, illegal_characters='$%^* '):
    for char in illegal_characters:
        if char in name:
            return True


def fix_chars(name,
              illegal_characters=None,
              replacement_char='-'):
    if illegal_characters is None:
        illegal_characters = ['$', '%', '^', '*', ' ']
    new_name = ""
    for x in name:
        if x in illegal_characters:
            new_name += replacement_char
        else:
            new_name += x
    return new_name


def join_paths_wrap(prefix_msg, root, name):
    return prefix_msg + os.path.join(root, name)


valid_replace_args = ['-r', '--replace']
if len(sys.argv) == 2 or len(sys.argv) == 3:
    root = sys.argv[1]
    for root, dirs, files in os.walk(root, topdown=True):
        for name in files:
            if illegal_characters(name) is True:
                os.rename(join_paths_wrap('', root, name),
                          join_paths_wrap('', root, fix_chars(name)))
        for name in dirs:
            if illegal_characters(name) is True:
                os.rename(join_paths_wrap('', root, name),
                          join_paths_wrap('', root, fix_chars(name)))

    for root, dirs, files in os.walk(root, topdown=True):
        for name in files:
            if illegal_length(name) is True:
                print(join_paths_wrap("Too long -->", root, name))
            if illegal_characters(name) is True:
                print(join_paths_wrap("Illegal chars -->", root, name))
        for name in dirs:
            if illegal_length(name) is True:
                print(join_paths_wrap("Too long -->", root, name))
            if illegal_characters(name) is True:
                print(join_paths_wrap("Illegal chars -->", root, name))
else:
    print("illegal number of arguments!!!")
