site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def find_key(struct, key, value):
    if key in struct:
        struct[key] = value
        return site

    for el in struct.values():
        if isinstance(el, dict):
            result = find_key(el, key, value)
            if result:
                return site


def new_sites(site, count):
    if count == 0:
        return site

    name = input('Введите название для нового сайта: ')
    keys = {'title': 'Куплю/продам {0} недорого'.format(name), 'h2': 'У нас самая низкая цена на {0}'.format(name)}

    for key, value in keys.items():
        find_key(site, key, value)

    print('Сайт для {0}:'.format(name))
    print(site, '\n')

    new_sites(site, count - 1)
    return site


site_count = int(input('Сколько сайтов: '))
new_sites(site, site_count)