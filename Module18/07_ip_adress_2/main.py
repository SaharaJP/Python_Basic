def is_four_num():
    if len(ip_address) != 4:
        print('Адрес - это четыре числа, разделенные точками. '
              '\nПопробуйте ввести адрес заново')
    else:
        return True

def is_integer():
    for index in ip_address:
        if not index.isdigit():
            print('{} - это не целое число'
                  '\nПопробуйте ввести адрес заново'.format(index))
            return False
    return True

def is_num_allowed():
    for i in ip_address:
        if int(i) > 255:
            print('{} превышает 255'
                  '\nПопробуйте ввести адрес заново'.format(i))
            return False
    return True


while True:
    ip_address = input('\nВведите IP: ').split('.')

    if is_four_num():
        if is_integer():
            if is_num_allowed():
                break

print('IP-адрес корректен')