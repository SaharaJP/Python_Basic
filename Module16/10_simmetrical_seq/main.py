num_count = int(input('Кол-во чисел: '))
subsequence = []
need_to_add = []

for _ in range(num_count):
    num = int(input('Число: '))
    subsequence.append(num)

if subsequence[-1] == subsequence[-2] and subsequence[-1] != subsequence[-3]:
    for i in range(len(subsequence) - 3, -1, -1):
        need_to_add.append(subsequence[i])

elif subsequence[-1] != subsequence[-2]:
    for i in range(len(subsequence) - 2, -1, -1):
        need_to_add.append(subsequence[i])

print('\nПоследовательность:', subsequence)
print('Нужно приписать чисел:', len(need_to_add))
print('Сами числа:', need_to_add)