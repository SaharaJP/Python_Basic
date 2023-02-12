from typing import Callable
import functools


class PermissionError(Exception):
    def __str__(self):
        return 'У пользователя недостаточно прав, чтобы выполнить функцию '


def check_permission(name: str) -> Callable:
    def permission_decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wr_permission(*args, **kwargs) -> None:
            try:

                if name in user_permissions:
                    func(*args, **kwargs)
                else:
                    raise PermissionError

            except PermissionError as ex:
                print(ex.__class__.__name__, end=': ')
                print(ex, end=func.__name__)

        return wr_permission
    return permission_decorator


user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()