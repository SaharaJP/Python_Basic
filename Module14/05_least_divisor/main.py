
def min_divider():
    for divider in range(2, number + 1):
        if number % divider == 0:
            print('Наименьший общий делитель:', divider)
            break


number = int(input('Введите число: '))

min_divider()