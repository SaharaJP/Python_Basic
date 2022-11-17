len_sum = 0
line_count = 0

with open('people.txt', 'r', encoding = 'utf-8') as names:
    for i_name in names:
        line_count += 1
        try:
            if (len(i_name) - 1) > 3:
                len_sum += len(i_name) - 1
            else:
                raise BaseException
        except BaseException:
            print('Ошибка: менее трёх символов в строке {0}'.format(line_count))

    print('Общее количество символов:', len_sum)
