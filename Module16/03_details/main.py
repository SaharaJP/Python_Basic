shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name = input('Название детали: ')
detail_count = 0
all_detail_cost = 0

for i in range(len(shop)):
        if shop[i][0] == detail_name:
                detail_count += 1
                all_detail_cost += shop[i][1]

print('Кол-во деталей -', detail_count)
print('Общая стоимость -', all_detail_cost)