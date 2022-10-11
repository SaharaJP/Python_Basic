import random

N = int(input('Введите максимальное число: '))
rand_num = random.randint(1, N)

while True:
    nums = input('\nНужное число есть среди вот этих чисел: ').split()

    if nums[0] == 'Помогите!':
        print('Артем мог загадать следующие числа:', in_set.difference(not_in_set))
        break

    num_set = set(
        {int(cyfer)
         for cyfer in nums}
    )

    if rand_num in num_set:
        print('Ответ Артема: Да')
        in_set = num_set
    else:
        print('Ответ Артема: Нет')
        not_in_set = num_set