main_list = [1, 5, 3]
first_side_list = [1, 5, 1, 5]
second_side_list = [1, 3, 1, 5, 3, 3]

main_list.extend(first_side_list)
print('Кол-во цифр 5 при первом объединении:', main_list.count(5))

for num in main_list:
    if num == 5:
        main_list.remove(5)

main_list.extend(second_side_list)
print('Кол-во цифр3 при втором объединении:', main_list.count(3))
print('Итоговый список:', main_list)