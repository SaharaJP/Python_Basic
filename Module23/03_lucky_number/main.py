import random

total_num = 0

with open('out_file.txt', 'w') as file:
    try:
        while True:
            num = input('Введите число: ')
            total_num += int(num)

            if random.randint(1, 14) == 13:
                raise BaseException

            file.write(num + '\n')

            if total_num >= 777:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                break

    except BaseException:
        print('Вас поститгла неудача')