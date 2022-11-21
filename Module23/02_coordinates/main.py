import random

def error_mess():
    cont_ask = input('Желаете продолжить? (Y/N) ').lower()
    if cont_ask == 'y':
        return 0
    elif cont_ask == 'n':
        print('Программа завершена')
        raise
    else:
        print('Введен несоответствующий ответ, программа завершена')
        raise

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    file = open('coordinates.txt', 'r')
    file_2 = open('result.txt', 'w')

    for line in file:
        nums_list = line.split()

        try:
            if f(int(nums_list[0]), int(nums_list[1])):
                res1 = f(int(nums_list[0]), int(nums_list[1]))

        except ZeroDivisionError:
            print('В первой функции произошло деление на "0". \n'
                  'Можно продолжить, приняв значение равное "0". \n')
            res1 = error_mess()
        except IndexError:
            print('В строке отсутствует "X" или "Y". \n'
                  'Можно продолжить, приняв значение равное "0". \n')
            res1 = error_mess()

        try:
            if f2(int(nums_list[0]), int(nums_list[1])):
                res2 = f2(int(nums_list[0]), int(nums_list[1]))

        except BaseException:
            print('Во второй функции функции произошло деление на "0" \n'
                  'Можно продолжить, приняв значение равное "0". \n')
            res2 = error_mess()
        except IndexError:
            print('В строке отсутствует "X" или "Y". \n'
                  'Можно продолжить, приняв значение равное "0". \n')
            res2 = error_mess()

        number = random.randint(0, 100)
        my_list = sorted([res1, res2, number])

        file_2.write(' '.join(str(sym) for sym in my_list))
        file_2.write('\n')

finally:
    file.close()
    file_2.close()