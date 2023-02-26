import re

num_list = ['9999999999', '999999-999', '99999x9999']
num_pattern = r'[89]\d{9}'

for num in num_list:
    if re.match(num_pattern, num):
        print(num_list.index(num) + 1, 'номер: все в порядке')
    else:
        print(num_list.index(num) + 1, 'номер: не подходит')
