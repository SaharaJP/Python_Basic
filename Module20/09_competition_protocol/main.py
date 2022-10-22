record_count = int(input('Сколько записей вносится в протокол? '))
score_dict = dict()
count = 0

print('Записи (результат и имя):')

for num in range(1, record_count + 1):
    record = input('{0}-я запись: '.format(num)).split()

    if int(record[0]) > score_dict.get(record[1], 0):
        score_dict[record[1]] = int(record[0])


print('\nИтоги соревнований:')

for place in range(1, 4):
    max_score = max(score_dict.values())

    for i_name, i_score in score_dict.items():
        if max_score == i_score:
            print('{0}-e место.'.format(place), i_name, i_score)
            break

    score_dict.pop(i_name)


