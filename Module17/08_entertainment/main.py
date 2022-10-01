import random

N = ['I' for _ in range(int(input('Количество палок: ')))]
throw_count = int(input('Количество бросков: '))

for throw in range(throw_count):
    left_i = random.randint(1, len(N))
    right_i = random.randint(left_i, len(N))
    print('Бросок ' + str(throw + 1) + '. Сбиты палки с номера', left_i,
          'по номер', right_i)
    N[left_i - 1 : right_i] = ['.' for _ in range(right_i - left_i + 1)]

print('\nРезультат:', end = '')
for i in N:
    print(i, end = '')