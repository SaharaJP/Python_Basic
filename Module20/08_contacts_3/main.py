def new_contact():
    names = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split())

    if current_dict.get(names):
        print('Такой человек уже есть в контактах.')
        return

    else:
        phone_num = int(input('Введите номер телефона: '))
        current_dict[names] = phone_num

        return current_dict

def find_contact():
    surname = input('Введите фаимилию для поиска: ').title()

    for i_key, i_value in current_dict.items():
        if surname in i_key:
            return i_key, i_value

    else:
        return


current_dict = dict()

while True:
    action = int(input('\nВведите номер действия: \n'
                       ' 1. Добавить контакт \n'
                       ' 2. Найти человека \n'))

    if action == 1:
        new_contact()
        print('Текущий словарь контактов', current_dict)

    elif action == 2:
        info = find_contact()

        if info:
            print(info[0][0], info[0][1], info[1])

        else:
            print('Человека с такой фамилией нет в словаре')