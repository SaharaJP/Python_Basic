pair_count = int(input('Введите количество человек: '))
pair_dict = dict()
lenght = 0

for count in range(1, pair_count):
    pair = input('{0} пара: '.format(count)).split()

    if not pair[1] in pair_dict:
        pair_dict[pair[1]] = lenght
    if not pair[0] in pair_dict:
        pair_dict[pair[0]] = pair_dict[pair[1]] + 1

print('\n"Высота" каждого члена семьи:')
for man in sorted(pair_dict):
    print(man, pair_dict[man])

