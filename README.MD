***Disclaimer***: This can damage file and folder names if used incorrectly or carelessly. I am not responsible for damage.

**Purpose**: This program takes in a directory, $root_dir, and checks the absolute path of every subfile/subfolder for the following violations:
- violation: path is 250 characters or longer
- violation: path contains the following illegal characters: '$', '%', '^', '*', or a space. Script easily modified to check for a different set of illegal characters.
  - optionally replaces illegal characters with `replace_char='-'`. `-` is the default. See **How to Run** below.

**How to run**: `python3 path_compliance.py /path/to/folder` where `/path/to/folder` is the $root_dir you are interested in.
- optionally run with `-r` or `--replace` to automatically replace illegal characters with `replace_char`. `replace_char='-'` for now but this is script is easily modifed to replace illegal characters with some other desired character.

**Contribute**: Please! Fork and PR as you wish! 
