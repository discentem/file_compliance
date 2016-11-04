import os
import sys
import re

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


def main(log_file="compliance_log.txt"):
    valid_replace_args = ['-r', '--replace']
    if len(sys.argv) == 2 or len(sys.argv) == 3 or len(sys.argv) == 4:
        root = sys.argv[1]
        try:
            if sys.argv[2] in valid_replace_args:
                for root, dirs, files in os.walk(root, topdown=True):
                    for name in files:
                        if illegal_characters(name) is True:
                            os.rename(join_paths_wrap('', root, name),
                                      join_paths_wrap('',
                                                      root,
                                                      fix_chars(name)))
                    for name in dirs:
                        if illegal_characters(name) is True:
                            os.rename(join_paths_wrap('', root, name),
                                      join_paths_wrap('',
                                                      root,
                                                      fix_chars(name)))
        except IndexError:
            pass

        f = open(log_file, "w")
        for root, dirs, files in os.walk(root, topdown=True):
            for name in files:
                if illegal_length(name) is True:
                    log_msg = join_paths_wrap("Too long -->", root, name)
                    f.write(log_msg + "\n")
                    print(log_msg)
                if illegal_characters(name) is True:
                    log_msg = join_paths_wrap("Illegal chars -->", root, name)
                    f.write(log_msg + "\n")
                    print(log_msg)
            for name in dirs:
                if illegal_length(name) is True:
                    log_msg = join_paths_wrap("Too long -->", root, name)
                    f.write(log_msg + "\n")
                    print(log_msg)
                if illegal_characters(name) is True:
                    log_msg = join_paths_wrap("Illegal chars -->", root, name)
                    f.write(log_msg + "\n")
                    print(log_msg)
        f.close()
    else:
        print("illegal number of arguments!!!")

try:
    log_file = sys.argv[3]
    try:
        os.remove("compliance_log.txt")
    except:
        pass
    main(log_file)
except IndexError:
    main()
