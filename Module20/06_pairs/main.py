import random

original_list = list(
    random.randint(0, 100)
    for _ in range(10)
)

new_list = list()

for num in range(len(original_list)):

    if num % 2 == 1:
        new_tuple = original_list[num - 1], original_list[num]
        new_list.append(new_tuple)

print(new_list)
