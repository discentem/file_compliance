***Disclaimer***: This can damage file and folder names if used incorrectly or carelessly. I am not responsible for damage.

**Purpose**: This program takes in a directory, $root_dir, and checks the absolute path of every subfile/subfolder for the following violations and logs to a file, by default `log.txt`:
- violation: path is 250 characters or longer
- violation: path contains the following illegal characters: '$', '%', '^', '*' or a space. Script easily modified to check for a different set of illegal characters.
  - optionally replaces illegal characters with `replace_char='-'`. `-` is the default. See **How to Run** below.

**How to run**: `python3 path_compliance.py -d /path/to/folder` where `/path/to/folder` is the root directory you are interested in. `-d` is a required argument.
- optional arguments:
  - `-l <file.txt>` or `--log <file.txt>`, where `file.txt` is the name of the file where you want to log violations.
  - `-c` or `--correct` to automatically replace illegal characters with `-`.

**Contribute**: Please! Fork and PR as you wish!
