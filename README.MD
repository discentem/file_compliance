**Disclaimer**: This can damage file and folder names if used without careful consideration.

**Purpose**: This program takes in a directory, $root_dir, and checks the absolute path of every file/folder for the following violations:
- violation: path is < 250 characters longer
- violation: path contains the following illegal characters: [$, %, ^, * ]
  - optionally replaces illegal characters with `replace_char='-'`. `-` is the default. See **How to Run** below.

**How to run**: `python3 path_compliance.py /path/to/folder` where `/path/to/folder` is the root folder you are interested in.
- optionally run `python3 path_compliance.py /path/to/folder -r` or `python3 path_compliance.py /path/to/folder --replace` to automatically replace illegal characters with whatever `replace_char` is. By default `replace_char='-'`.

**Notes**: NOT recursive yet. Only deals with paths at the top level. Fixing this asap.
