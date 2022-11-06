import os

text = input('Введите строку: ')
save_path = input('\nКуда хотите сохранить документ? Введите полседовательность папок (через пробел): ').title().split()
file_name = input('\nВведите имя файла: ') + '.txt'

save_path = '\\'.join(save_path)
path = os.path.join('D:\\', save_path)

if os.path.exists(path):
    os.chdir(path)
    file = open(file_name, 'w', encoding = 'utf-8')

    if file_name in os.listdir():
        r_u_sure = input('Вы действительно хотите перезаписать файл? (Да / Нет) ').lower()
        if r_u_sure == 'да':
            file.write(text)
            print('Файл успешно перезаписан!')

    else:
        file.write(text)
        print('Файл успешно сохранен!')

    file.close()

else:
    print('Такого пути не существует.')