
def point_counting(num): #Записывает число знаков после запятой
    count = 0
    while num - round(num) > 0:
        num *= 10
        count += 1
    return count


def backward_counting(num): #Записывает число наоборот
    backward = ''
    for back_num in str(num):
        backward = back_num + backward
    return backward


def backward_num(num):
    before_point = round(num)
    after_point = num - before_point

    back_before_point = float(backward_counting(before_point))
    back_after_point = float(backward_counting(round(after_point, 10)))
    divider = point_counting(num)

    backward_num = back_before_point + back_after_point / (10 ** divider)
    return backward_num


first_num = float(input('Введите первое число: '))
second_num = float(input('Введите второе число: '))

first_backward_num = backward_num(first_num)
second_backward_num = backward_num(second_num)

print('\nПервое число наоборот:', first_backward_num)
print('Второе число наоборот:', second_backward_num)
print('Сумма:', first_backward_num + second_backward_num)