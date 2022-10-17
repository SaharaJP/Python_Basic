students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def info(dict):
    pairs = [
        (id, param.get('age', {}))
        for id, param in dict.items()
    ]

    interests = set(
        j_inter
        for i_value in dict.values()
        for j_inter in i_value['interests']
    )

    surname = 0
    for i_value in dict.values():
        surname += (len(i_value.get('surname')))

    return pairs, interests, surname


my_lst = info(students)

print('Список пар "ID студента - возраст":', my_lst[0])
print('Полный список интересов всех студентов:', my_lst[1])
print('Общая длина всех фамилий студентов:', my_lst[2])