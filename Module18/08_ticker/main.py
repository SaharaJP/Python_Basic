f_string = input('Первая строка: ')
s_string = input('Вторая строка: ')
count = 0

for i in range(1, len(f_string) + 1):
    if s_string.endswith(f_string[:i]) and s_string.startswith(f_string[i:]):
        print('Первая строка получается из второй со сдвигом', i)
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')