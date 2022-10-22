string = 'abcd'
nums_tuple = (10, 20, 30, 40)
result_list = list()

print('Строка:', string)
print('Кортеж чисел:', nums_tuple)

print('\nРезультат:')
for i in range(min(len(string), len(nums_tuple))):
    result_list.append((string[i], nums_tuple[i]))

for part in result_list:
    print(part)