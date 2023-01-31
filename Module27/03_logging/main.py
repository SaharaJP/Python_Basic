from typing import Callable
import functools
import datetime

def logging(func: Callable) -> Callable:
    """Декоратор. Отвечает за логирование функций"""

    @functools.wraps(func)
    def wr_log() -> None:
        with open('function_errors.log', 'a') as errors:
            try:
                func()
            except ZeroDivisionError:
                print(
                    '{name} - {document}\n'.format(
                        name=func.__name__,
                        document=func.__doc__
                    )
                )
                errors.write(
                    '{time}\t{name}\t{error}\n'.format(
                        time=str(datetime.datetime.now()),
                        name=func.__name__,
                        error=str(ZeroDivisionError)
                    )
                )
    return wr_log

@logging
def math_error():
    """Функция, вызывающая ошибку деления на 0"""

    raise ZeroDivisionError

@logging
def math_error_2():
    """Функция, вызывающая ошибку деления на 0"""

    raise ZeroDivisionError


math_error()
math_error_2()