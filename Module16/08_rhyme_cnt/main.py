people = int(input('Кол-во человек: '))
rhyme = int(input('Какое число в считалке? '))
people_list = list(range(1, people+ 1))
out = 0

print('Значит, выбывает каждый ' + str(rhyme) + '-й человек.')

while len(people_list) > 1:
   print('\nТекущий круг людей', people_list)

   start = out % len(people_list)
   out = (start + rhyme - 1) % len(people_list)

   print('Начало счёта с номера', people_list[start])
   print('Выбывает человек под номером', people_list[out])

   people_list.remove(people_list[out])

print('Остался человек под номером', people_list[0])