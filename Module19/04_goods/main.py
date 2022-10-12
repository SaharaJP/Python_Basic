goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for good_name in goods:
    way = store[goods[good_name]]
    quantity = 0
    total_price = 0

    for num in range(len(way)):
        quantity += way[num]['quantity']
        total_price += way[num]['price'] * way[num]['quantity']

    print('{0} - {1} штук, стоимость {2} рубля'.format(
        good_name,
        quantity,
        total_price)
    )