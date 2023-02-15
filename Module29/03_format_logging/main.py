from typing import Callable
import functools
from datetime import datetime
import time


def date_decorator(cls, func: Callable, date_format: str) -> Callable:
    @functools.wraps(func)
    def wr_date_decorator(*args, **kwargs):
        form = date_format
        for sym in form:
            if sym.isalpha():
                form = form.replace(sym, '%' + sym)
        print(
            "- Запускается '{cls_name}.{func}'. Дата и время запуска: "
            "{date_format}".format(
                cls_name=cls.__name__,
                func=func.__name__,
                date_format=datetime.now().strftime(form)
            )
        )
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("- Завершение '{func}', время работы =".format(func=func.__name__), round(end - start, 3))
        return result
    return wr_date_decorator


def log_methods(date_format) -> Callable:
    """Декоратор класс. Декорирует все методы в классе"""
    def wr_decorator(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                cur_method = getattr(cls, method)
                decorated_method = date_decorator(cls, cur_method, date_format)
                setattr(cls, method, decorated_method)
        return cls
    return wr_decorator


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
