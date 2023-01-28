import os
from collections.abc import Iterable


def gen_line_count(dir: str) -> Iterable[str]:
    line_count = 0

    python_files = [
        paths + os.sep + file
        for paths, cats, files in os.walk(dir)
        for file in files
        if file.endswith('.py')
    ]

    for file in python_files:
        for line in open(file, 'r').readlines():
            if not line.startswith('#') or not line == '\n':
                line_count += 1
    else:
        return line_count


directory = os.path.abspath(os.path.join('..', '..','Module25'))
lines = gen_line_count(directory)
print(lines)
