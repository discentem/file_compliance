import os
import sys
import re

illegals = '$%^* '

def illegal_length(name, max_length=250):
    return len(name) > max_length:

def illegal_characters(name, illegal_characters=illegals):
    illegal = false
    for char in illegal_characters:
        illegal = char in name
    
    return illegal

def fix_chars(name,
              illegal_chars=illegals,
              replacement_char='-'):
    return ''.join([ str.replace(x, replacement_char) for x in name if x in illegal_chars ])


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
