import os
from collections.abc import Iterable


def gen_files_path(cat: str, dir: str = '/') -> Iterable[str]:
    for path, dir, file in os.walk(dir):
        yield path


directory = os.path.abspath(os.path.join('..', '..', '..', 'Python_Basic'))
gen = gen_files_path('Module16', directory)

for path in gen:
    print(path)