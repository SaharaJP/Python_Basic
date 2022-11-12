def first_tour_add_info():
    first_tour = open('first_tour.txt', 'w', encoding = 'utf-8')
    first_tour.write(input('Введите минимальный порог баллов для прохода во второй тур: ') + '\n')
    count = int(input('Введите число участников: '))

    for _ in range(count):
        first_tour.write(input('Введите имя, фамилию и число очков через пробел: ') + '\n')

    first_tour.close()

def second_tour_add_info():
    first_tour = open('first_tour.txt', 'r', encoding = 'utf-8')
    second_tour = open('second_tour.txt', 'w', encoding = 'utf-8')

    min_score = int(first_tour.readline())
    max_scores = [0]
    count = 0

    print('\nСодержимое фалйла {0}'.format('first_tour.txt'))
    for line in first_tour.readlines():
        print(line, end = '')
        line_dict = line.split()

        if int(line_dict[2]) > min_score:
            second_tour.write(line)
            max_scores.append(int(line_dict[2]))
            count += 1

    first_tour.close()
    second_tour.close()

    return count, max_scores
def second_tour_answer(count, max_scores):
    second_tour = open('second_tour.txt', 'r', encoding = 'utf-8')

    print('\nСодержимое фалйла {0}'.format('second_tour.txt'))
    print(count)

    for num in range(1, count + 1):
        second_tour.seek(0)

        for line in second_tour.readlines():
            participant_dict = line.split()

            if max(max_scores) == int(participant_dict[2]):
                max_scores.remove(max(max_scores))
                print('{0}) {1}.'
                      .format(num, participant_dict[1][0]),
                      participant_dict[0], participant_dict[2]
                      )

    second_tour.close()

first_tour_add_info()
count, max_scores = second_tour_add_info()
second_tour_answer(count, max_scores)