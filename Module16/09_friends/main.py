friends = int(input('Кол-во друзей: '))
credit = int(input('Долговых расписок: '))
balances = []

for i in range(friends):
    balances.append([i + 1, 0])

for i in range(credit):
    print('\n' + str(i + 1) + '-я расписка')
    friend_to = int(input('Кому: '))
    friend_from = int(input('От кого: '))
    how_much = int(input('Сколько: '))

    balances[friend_to - 1][1] -= how_much
    balances[friend_from - 1][1] += how_much

else:
    print('\nБаланс друзей:')
    for i in range(friends):
        print(balances[i][0], end = ' : ')
        print(balances[i][1])