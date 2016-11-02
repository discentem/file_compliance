import os
import sys


def list_files_in(root_dir):
    '''Returns a list of the full paths to
       files/folders contained in $root_dir.'''
    return [root_dir + f for f in os.listdir(root_dir)]


def check_length_violations(files, max_len=250):
    '''Returns a list of paths to files/folders contained in $files
       that are greater than 250 characters.'''
    violations = []
    for f in files:
        if len(f) >= max_len:
            violations.append(f)
    return violations


def find_occurences(s, ch):
    '''Returns the list of indexes where $ch occurs in $s

       s is assumed to be a string. ch is assumed to be a 1 character string.
    '''
    return [i for i, letter in enumerate(s) if letter == ch]


def check_illegal_chars(root, directories, illegal_characters,
                        replacement_char='-', replace=False):
    '''Returns a list of paths to files/folders in $root that contain
       characters specificed in $illegal_characters, a list.

       If replace==True, the illegal characters are replaced by
       replacement_char first list is returned.'''
    violations = []
    for directory in directories:
        for character in illegal_characters:
            for i in find_occurences(directory, character):
                if replace:
                    new_dir = directory[:i] + replacement_char + directory[i+1:]  # noqa
                    os.rename(directory, new_dir)
                    violations = check_illegal_chars(root,
                                                     directories,
                                                     illegal_characters)
                else:
                    violations.append(directory)

    return violations


def create_compliance_log(root,
                          illegal_chars,
                          replace_char='-',
                          max_len=250,
                          replace=False,
                          log_path='compliance_log.txt'):
    '''Logs paths to files/folders that have illegal characters or are longer
       than $max_len using above functions. Logs to $log_path.'''

    # list of all files in $root with full path
    files = list_files_in(root)
    # list of all files in $root with illegal characters
    directories_with_illegal_chars = check_illegal_chars(root,
                                                         files,
                                                         illegal_chars,
                                                         replacement_char=replace_char,  # noqa
                                                         replace=replace)
    # list of all files in $root that are too long
    directories_with_illegal_length = check_length_violations(files,
                                                              max_len=max_len)

    # writes to log all paths containing illegal characters
    f = open(log_path, 'w')
    for d in directories_with_illegal_chars:
        f.write('Illegal char: ' + d + '\n')

    # skips to spaces if len(directories_with_illegal_chars) > 0
    if len(directories_with_illegal_chars) > 0:
        f.write('\n'*2)

    # writes to log all paths > 250 chars
    for d in directories_with_illegal_length:
        f.write('Greater than ' + str(max_len) + ": " + str(d) + '\n')

    f.close()


def main():
    if len(sys.argv) == 3:
        root = sys.argv[1]
        replace = False
        try:
            valid_replace_arg = ['-r', '--replace']
            if sys.argv[3] in valid_replace_arg:
                replace = True
            else:
                raise ValueError("Incorrect flag.")
        except:
            pass
        illegal_chars = ['$', '%', '^', '*', ' ']
        create_compliance_log(root, illegal_chars, replace=replace)

    else:
        print("illegal number of arguments. Must have exactly 3.")


main()
