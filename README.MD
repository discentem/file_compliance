***Disclaimer***: This can damage file and folder names if used incorrectly or carelessly. I am not responsible for damage.

**Purpose**: This program takes in a directory and checks the absolute path of every subfile/subfolder (recursively) for the following violations and logs such violations to a file.
- violation: path is 250 characters or longer
- violation: path contains the following illegal characters: '$', '%', '^', '*' or a space. Script easily modified to check for a different set of illegal characters.
  - optionally replaces illegal characters with `replace_char='-'`. `-` is the default. See **How to Run** below.

**How to run**: `python3 main.py /path/to/folder` where `/path/to/folder` is the root directory you are interested in. `-d` is a required argument.
- optional arguments:
  - `-l file.txt` or `--log file.txt`, where `file.txt` is the name of the file where you want to log violations. If not specified, defaults to `log.txt`
  - `-c` or `--correct` to automatically replace illegal characters with `-`. (This flag needs no input.)

**Contribute**: Please! Fork and PR as you wish!
