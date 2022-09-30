import random

num_count = int(input('Количество чисел в списке: '))
num_list = [random.randint(0, 2) for _ in range(num_count)]

count = 0
for i in range(num_count):
    if num_list[i] > 0:
        num_list[i], num_list[count] = num_list[count], num_list[i]
        count += 1

num_list = num_list[:num_list.index(0)]

print('Список после сжатия:', num_list)
