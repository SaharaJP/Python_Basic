import functools


name_dict = dict()

def singleton(cls):
    @functools.wraps(cls)
    def wr_singleton(*args, **kwargs):
        if cls.__name__ not in name_dict.keys():
            name_dict[cls.__name__] = cls(*args, *kwargs)
        return name_dict[cls.__name__]
    return wr_singleton


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
