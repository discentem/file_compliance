**Disclaimer**: This can damage file and folder names if used without careful consideration.

**Purpose**: This program takes in a directory, $root_dir, and checks the absolute path of every file/folder for the following violations:
- violation: path is < 250 characters longer
- violation: path contains the following illegal characters: `[$, %, ^, * ]`. The illegal character list can be changed in `fix_chars()` or by explicitly passing `illegal_chars` to `fix_chars()`.
  - optionally replaces illegal characters with `replace_char='-'`. `-` is the default. See **How to Run** below.

**How to run**: `python3 path_compliance.py /path/to/folder` where `/path/to/folder` is the root folder you are interested in.
- optionally run with `-r` or `--replace` to automatically replace illegal characters with `replace_char`. By default `replace_char='-'`.
