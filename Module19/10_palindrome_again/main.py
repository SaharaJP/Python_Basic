text = input('Введите строку: ')
sym_dict = dict()

for sym in text:
    sym_dict[sym] = sym_dict.get(sym, 0) + 1

odd_count = 0
for value in sym_dict.values():
    if value % 2 != 0:
        odd_count += 1

if odd_count <= 1:
    print('Можно сделать палиндром')
else:
    print('Нельзя сделать палиндром')