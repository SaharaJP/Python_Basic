def w_n_cycles(num):
    if num == 0:
        return 1

    num = w_n_cycles(num - 1)
    print(num)

    return num + 1


num = int(input('Введите num: '))
w_n_cycles(num)