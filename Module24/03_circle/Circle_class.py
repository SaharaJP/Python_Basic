import math

class Circle:
    circles_dict = dict()
    count = 0

    def __init__(self, x = 0, y = 0, r = 1):
        Circle.count += 1
        self.name = self.count
        self.x = x
        self.y = y
        self.r = r

        self.circles_dict[self.count] = {
            'x' : self.x,
            'y' : self.y,
            'r' : self.r
        }


    def print_info(self):
        print('Данные по имеющимся окружностям: {0}'.format(self.circles_dict))

    def perimetr_func(self):
        perimetr = 2 * math.pi * self.r
        print('Периметр круга {0}: {1}'.format(self.name, perimetr))

    def square_func(self):
        square = math.pi * self.r ** 2
        print('Площадь круга {0}: {1}'.format(self.name, square))

    def increase_func(self):
        increase = int(input('Во сколько раз хотите увеличить круг? '))
        self.circles_dict[self.name]['r'] *= increase
        self.print_info()

    def intersection_func(self):
        for i_key, i_value in self.circles_dict.items():
            formule = math.sqrt((self.x - i_value['x']) ** 2 + (self.y - i_value['y']) ** 2)

            try:
                if formule <= (self.circles_dict[self.name]['r'] - i_value['r']) and i_key != self.name:
                    raise BaseException

                elif formule <= (i_value['r'] - self.circles_dict[self.name]['r']) and i_key != self.name:
                    raise BaseException

                elif formule >= (self.circles_dict[self.name]['r'] + i_value['r']) and i_key != self.name:
                    raise BaseException

            except BaseException:
                print('Окружности {0} и {1} пересекаются'.format(self.name, i_key))
                break

        else:
            print('Окружность не пересекается с другими')