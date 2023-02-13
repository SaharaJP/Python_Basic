import functools
from typing import Callable

app = dict()

def callback(route: str = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        app[route] = func

        @functools.wraps(func)
        def wr_decorator(*args, **kwargs):
            func_call = func(*args, **kwargs)
            return func_call
        return wr_decorator

    return decorator



@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')