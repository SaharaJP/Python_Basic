
def coin_area():
    if abs(x) - r <= 0 and abs(y) - r <= 0:
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')


print('Введите координаты монеты:')
x = float(input('X: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))

coin_area()