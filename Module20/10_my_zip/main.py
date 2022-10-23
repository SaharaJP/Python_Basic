string = 'abcd'
nums_tuple = (10, 20, 30, 40)

print('Строка:', string)
print('Кортеж чисел:', nums_tuple)

print('\nРезультат:')
result_list = ((string[i], nums_tuple[i])
               for i in range(min(len(string), len(nums_tuple))))

print(result_list)

for part in result_list:
    print(part)