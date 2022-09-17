
def same_numbers(): #Записывает годы с тремя одинаковыми цифрами
    for year in range(first_year, second_year + 1):
        count = 1
        new_year = year
        num = new_year % 10
        new_year //= 10
        while new_year > 0:
            new_num = new_year % 10
            if new_num == num:
                count += 1
            new_year //= 10
        if count == 3:
            print(year)


first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

print('\nГоды от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')

same_numbers()