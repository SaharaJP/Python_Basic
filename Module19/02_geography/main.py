def input_names():
    country_count = int(input('Количество стран: '))
    country_dict = dict()

    for i in range(country_count):
        country = input('Страна {0}: '.format(i + 1)).split()
        country_dict[country[0]] = set(country[1:])

    return country_dict


def is_city_in_country():
    for i in range(3):
        is_city_in = False
        city = input('\n{0} город: '.format(i + 1))

        for country in country_dict:
            if city in country_dict[country]:
                print('Город {0} расположен в стране {1}'.format(city, country))
                is_city_in = True

        if not is_city_in:
            print('По городу {0} данных нет'.format(city))


country_dict = input_names()
is_city_in_country()