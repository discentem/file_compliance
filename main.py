import os
import sys
import argparse

illegals = '$%^* '


def illegal_length(name, max_length=250):
    return len(name) > max_length


def illegal_characters(name, illegal_characters=illegals):
    for char in illegal_characters:
        if char in name:
            return True
    return False


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


def gather_args():
    parser = argparse.ArgumentParser()
    replace_help_msg = "Used to replace illegal characters automatically"
    parser.add_argument('directory')
    parser.add_argument('-c', "--correct", default='',
                        dest='reset',
                        action='store_true',
                        help=replace_help_msg)
    parser.add_argument('-l', '--log', dest="log",
                        default="compliance_log.txt")
    return parser.parse_args()

args = gather_args()
f = open(args.log, "w")
directory = args.directory
if args.reset:
    for root, dirs, files in os.walk(directory, topdown=True):
        for name in files:
            if illegal_characters(name) is True:
                os.rename(join_paths_wrap('', root, name),
                          join_paths_wrap('', root, fix_chars(name)))
        for name in dirs:
            if illegal_characters(name) is True:
                os.rename(join_paths_wrap('', root, name),
                          join_paths_wrap('', root, fix_chars(name)))

for root, dirs, files in os.walk(directory, topdown=True):
    for name in files:
        if illegal_length(name) is True:
            f.write(join_paths_wrap("Too long -->", root, name) + "\n")
        if illegal_characters(name) is True:
            f.write(join_paths_wrap("Illegal chars -->", root, name) + "\n")  # noqa
    for name in dirs:
        if illegal_length(name) is True:
            f.write(join_paths_wrap("Too long -->", root, name) + "\n")
        if illegal_characters(name) is True:
            f.write(join_paths_wrap("Illegal chars -->", root, name) + "\n")  # noqa
