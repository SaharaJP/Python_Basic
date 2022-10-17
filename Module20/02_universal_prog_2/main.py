def crypto(data):
    return [
        value
        for index, value in enumerate(data[1])
        if index in data[0]
    ]

def is_prime(object):
    prime_num_list = list()

    for index, value in enumerate(object):
        prime_num = True

        for num in range(2, (index // 2) + 1):
            if index % num == 0:
                prime_num = False
                break

        if index >= 2 and prime_num == True:
            prime_num_list.append(index)

    return prime_num_list, object


prime_n_object = is_prime('О Дивный Новый мир!')
answer = crypto(prime_n_object)

print(answer)