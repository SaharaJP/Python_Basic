from typing import Callable
import functools


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор. Спрашивает как дела у пользователя и
    выводит выводит ответ как дела у него
    """

    @functools.wraps(func)
    def wraped(*args, **kwargs) -> int:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)

        return result
    return wraped


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def squares_sum(num: int) -> int:
    """Функция, возвращает сумму квадратов"""

    result = 0
    for _ in range(num):
        result += sum([i ** 2 for i in range(10)])
    return result


test()
print()

result = squares_sum(10)
print(result)