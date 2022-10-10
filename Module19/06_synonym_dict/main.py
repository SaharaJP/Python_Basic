pair_count = int(input('Введите количество пар слов: '))
pairs_dict = dict()

for num in range(pair_count):
    pair = input('{0} пара: '.format(num + 1)).split(' - ')
    pairs_dict[pair[0]] = pair[1]

while True:
    word = input('\nВведите слово (для выхода введите "end"): ').lower()

    if word == 'end':
        break

    for sin in pairs_dict:
        if pairs_dict[sin].lower() == word:
            print('Синоним:', sin)
            break

        elif sin.lower() == word:
            print('Синоним:', pairs_dict[sin])
            break
    else:
        print('Такого слова в словаре нет')

