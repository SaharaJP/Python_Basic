guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)

    guest_action = input('Гость пришел или ушел? ')
    if guest_action == 'Пора спать':
        break

    guest_name = input('Имя гостя: ')

    if guest_action == 'пришел':
        if len(guests) < 6:
            print('Привет, ' + guest_name + '!')
            guests.append(guest_name)
        else:
            print('Прости, ' + guest_name + ', но мест нет.')
    elif guest_action == 'ушел':
        print('Пока, ' + guest_name + '!')
        guests.remove(guest_name)

print('\nВечеринка закончилась, все легли спать.')