skates_count = int(input('Кол-во коньков: '))
skates_pairs_sizes = []

for pair in range(skates_count):
    print('Размер ' + str(pair + 1) + '-й пары:', end = ' ')
    pair_size = int(input())
    skates_pairs_sizes.append(pair_size)

people_count = int(input('\nКол-во людей: '))
people_legs_sizes = []

for legs in range(people_count):
    print('Размер ' + str(legs + 1) + '-й пары:', end=' ')
    legs_size = int(input())
    people_legs_sizes.append(legs_size)

count = 0
for _ in range(people_count):
    if max(skates_pairs_sizes) >= max(people_legs_sizes):
        skates_pairs_sizes.remove(max(skates_pairs_sizes))
        people_legs_sizes.remove(max(people_legs_sizes))
        count += 1

    elif max(skates_pairs_sizes) <= max(people_legs_sizes):
        people_legs_sizes.remove(max(people_legs_sizes))

    elif max(skates_pairs_sizes) >= min(people_legs_sizes):
        skates_pairs_sizes.remove(max(skates_pairs_sizes))
        people_legs_sizes.remove(min(people_legs_sizes))
        count += 1


print('\nНаибольшее кол-во людей, которые могут взять ролики:', count)