def move(n, x, y, z):
    if n == 0:
        return

    move(n - 1, x, z, y)
    print('Переложить диск {0} со стержня {1} на стержень номер {2}'.format(n, x, z))
    move(n - 1, y, x, z)

    return

num = int(input('Введите число дисков: '))
move(num, 1, 2, 3)