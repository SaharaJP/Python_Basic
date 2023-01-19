class Second:
    __main_num = 0

    def __init__(self, num):
        self.__num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.__main_num < self.__num:
            self.__main_num += 1
            return self.__main_num ** 2
        else:
            raise StopIteration

def third(num):
    main_num = 0

    for _ in range(num):
        main_num += 1
        yield main_num ** 2


first_gen = (num ** 2 for num in range(1, int(input('Введите число: ')) + 1))
second_gen = Second(int(input('Введите число: ')))
third_gen = third(int(input('Введите число: ')))

for i_first in first_gen:
    print(i_first, end = ' ')
print('\n')

for i_second in second_gen:
    print(i_second, end = ' ')
print('\n')

for i_third in third_gen:
    print(i_third, end = ' ')