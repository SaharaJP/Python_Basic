from typing import Callable
import functools


def counter(func: Callable) -> Callable:
    """Декоратор. Считает и выводит, сколько раз вызвали функцию"""

    @functools.wraps(func)
    def wr_count() -> None:
        wr_count.count += 1
        func()
        print(
            'Функцию {name} вызвали {count} раз(а)'.format(
                name=func.__name__,
                count=wr_count.count
            )
        )

    wr_count.count = 0
    return wr_count


@counter
def first() -> None:
    pass

@counter
def second() -> None:
    pass

first()
second()

first()
first()