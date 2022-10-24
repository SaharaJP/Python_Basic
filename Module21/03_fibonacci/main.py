def fibo(num):
    if num in (1, 2):
        return 1

    return fibo(num - 1) + fibo(num - 2)


num_pos = int(input('Введите позиция в ряде Фибоначчи: '))
print('Число', fibo(num_pos))