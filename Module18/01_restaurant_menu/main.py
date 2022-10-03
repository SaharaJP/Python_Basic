available_menu = input('Доступное меню (осуществляйте ввод через ";"): ').split(';')
available_menu_str = ', '.join(available_menu)

# print('На данный момент в меню есть:', ', '.join(available_menu))
print('На данный момент в меню есть:', available_menu_str)