import os
import sys


def list_files_in(root_dir):
    '''Returns a list of the full paths to
       files/folders contained in $root_dir.'''
    return [root_dir + "/" + f for f in os.listdir(root_dir)]


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

    print(directories_with_illegal_length)

    f = open(log_path, 'w')
    for d in directories_with_illegal_chars:
        f.write('illegal char: ' + d + '\n')
    f.write('\n'*2)
    for d in directories_with_illegal_length:
        f.write('!!Greater than ' + str(max_len) + ": " + str(d) + '\n')

    f.close()


def main():
    root = '/Users/Brandon/Desktop/file_compliance/testing'
    illegal_chars = ['$', '%', '^', '*', ' ']

    create_compliance_log(root, illegal_chars, replace=False)

main()
