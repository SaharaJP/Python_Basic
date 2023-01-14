class Auto:
    def __str__(self):
        return '\nАвтомобиль расположен по координатам:\n' \
               'X: {0}\n' \
               'Y: {1}\n'.format(
            self.__x, self.__y
        )

    def __init__(self, x = 0, y = 0, direction = 'w', distance = 0):
        self.__x = x
        self.__y = y
        self.move(direction, distance)

    def move(self, direction, distance):
        if direction == 'w':
            self.__y += distance
        elif direction == 's':
            self.__y -= distance
        elif direction == 'd':
            self.__x += distance
        elif direction == 'a':
            self.__x -= distance

    def get_x(self):
        return self.__x

    def set_x(self, new_x):
        self.__x = new_x

    def get_y(self):
        return self.__y

    def set_y(self, new_y):
        self.__y = new_y

class Bus(Auto):
    cost = 2

    def __init__(self, x = 0, y = 0, direction = 'w',
                 distance = 0, passengers = 0, money = 0):
        self.__passengers = passengers
        self.__money = money
        super().__init__(x, y, direction, distance)

    def in_passenger(self):
        in_passengers = int(input('Автобус прибыл на остановку\n'
                                  'Сколько пассажиров зашло в автобус? '))
        self.__passengers += in_passengers

    def out_passenger(self):
        out_passengers = int(input('Сколько пассажиров вышло из автобуса? '))
        self.__passengers -= out_passengers

    def get_passengers(self):
        return 'Количество пассажиров: {0}'.format(self.__passengers)

    def get_money(self):
        return 'Количество денег: {0}'.format(self.__money)

    def move(self, direction, distance):
        super().move(direction, distance)
        self.__money += distance * self.__passengers * self.cost

        print(self.__str__())
        self.in_passenger()
        self.out_passenger()


auto = Auto(distance=10)
auto.move('a', 14)
print(auto)


bus = Bus(distance=5, passengers=7)
bus.move('w', 50)
print(bus.get_passengers())
print(bus.get_money())