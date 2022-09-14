def summ(num):
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10
    print('\nСумма чисел:', summ)
    return summ

def count_num(num):
    count = 0
    for cifer_summ in num:
        count += 1
    print('Количество цифр в числе:', count)
    return count


num = int(input('Введите число: '))
difference = summ(num) - count_num(str(num))

print('Разность суммы и количество цифр:', difference)