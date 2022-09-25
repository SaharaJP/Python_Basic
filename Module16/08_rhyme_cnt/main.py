people_count = int(input('Кол-во человек: '))
people_count = list(range(1, people_count + 1))
rhyme = int(input('Какое число в считалке? '))
start = 1
count = 0

print('Значит, выбывает каждый ' + str(rhyme) + '-й человек')
print('\nТекущий круг людей:', people_count)
print('Начало счета с номера', start)

# while count < rhyme:
#     for num in people_count:
#         count += 1
#         if count == rhyme:
#             people_count.remove(num)

while len(people_count) > 1:

    if rhyme > len(people_count):
        people_count.remove(abs(rhyme - len(people_count)))
    else:
        people_count.remove(rhyme)
    print(people_count)