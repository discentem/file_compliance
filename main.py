import os
import sys
import re

illegals = ['$', '%', '^', '*', ' ']


def illegal_length(name, max_length=250):
    return len(name) > max_length


def illegal_characters(name, illegal_characters=illegals):
    for char in illegal_characters:
        if char in name:
            return True

    return false


def fix_chars(name,
              illegal_chars=illegals,
              replacement_char='-'):
    new_name = ""
    for x in name:
        if x in illegal_chars:
            new_name += replacement_char
        else:
            new_name += x
    return new_name


def join_paths_wrap(prefix_msg, root, name):
    return prefix_msg + os.path.join(root, name)


valid_replace_args = ['-r', '--replace']
if len(sys.argv) == 2 or len(sys.argv) == 3:
    root = sys.argv[1]
    try:
        if sys.argv[2] in valid_replace_args:
            for root, dirs, files in os.walk(root, topdown=True):
                for name in files:
                    if illegal_characters(name) is True:
                        os.rename(join_paths_wrap('', root, name),
                                  join_paths_wrap('', root, fix_chars(name)))
                for name in dirs:
                    if illegal_characters(name) is True:
                        os.rename(join_paths_wrap('', root, name),
                                  join_paths_wrap('', root, fix_chars(name)))
    except IndexError:
        pass

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
