from typing import Callable
import functools
import time


def sleep_timer(func: Callable) -> Callable:
    """Декоратор. Ожидающий перед выполнением функции несколько секунд"""

    @functools.wraps(func)
    def wraped() -> None:
        time.sleep(3)
        func()

    return wraped

@sleep_timer
def test() -> None:
    """Тестовая функция"""

    print('Hello')


test()