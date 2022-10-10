order_counts = int(input('Введите количество заказов: '))
orders_dict = dict()

for count in range(order_counts):
    order = input('{0} заказ: '.format(count + 1)).split()
    order[2] = int(order[2])

    if not order[0] in orders_dict:
        orders_dict[order[0]] = {order[1] : order[2]}

    elif order[1] in orders_dict[order[0]]:
        orders_dict[order[0]][order[1]] += order[2]

    else:
        orders_dict[order[0]].update({order[1] : order[2]})

print()
for name in orders_dict:
    print(name + ':')
    for order in orders_dict[name]:
        print('\t\t' + order + ':', orders_dict[name][order])