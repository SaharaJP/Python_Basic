not_allowed_sym = '@№$%^&\*()'
allowed_extencions = ['.txt', '.docx']

file_name = input('Введите название файла: ')

for sym in not_allowed_sym:
    if file_name.startswith(sym):
        print('Ошибка: название начинается на один из специальных символов')
        break

for extencions in allowed_extencions:
    if not file_name.endswith(extencions):
        print('Ошибка: неверное расширение файла. Ожидалось ".txt" или ".docx"')
        break
    else:
        print('Файл назван верно')
        break