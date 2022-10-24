site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def key_value(struct, key, deep = -1):
    if deep == 0:
        return

    if key in struct:
        return struct[key]

    for el in struct.values():
        if isinstance(el, dict):
            result = key_value(el, key, deep - 1)
            if result:
                break
    else:
        result = None

    return result

def deep_func():
    while True:
        want_deep = input('Хотите ввести максимальную глубину? Y/N: ').lower()

        if want_deep == 'y':
            max_deep = int(input('Введите максимальную глубину: '))
            key = key_value(site, find_key, max_deep)
            return key

        elif want_deep == 'n':
            key = key_value(site, find_key)
            return key

        else:
            print('Ошибка, введите Y или N')


find_key = input('Введите искомый ключ: ')
result = deep_func()

print('Значение ключа:', result)