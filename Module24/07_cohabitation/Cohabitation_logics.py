import random

class Tenant:
    count = 1
    def __init__(self, name):
        if name == '':
            name = 'Жилец {0}'.format(self.count)
        self.name = name
        self.satiety = 50
        Tenant.count += 1

    def do_eat(self):
        House.food -= 5
        self.satiety += 10

        if House.food < 0:
            Cohabitation.is_alive = False

    def do_work(self):
        House.money += 20
        self.satiety -= 10

        if self.satiety < 0:
            Cohabitation.is_alive = False

    def do_play(self):
        self.satiety -= 10

        if self.satiety < 0:
            Cohabitation.is_alive = False

    def do_shop(self):
        House.food += 10
        House.money -= 10

        if House.money < 0:
            Cohabitation.is_alive = False

class House:
    food = 50
    money = 0

class Cohabitation:
    is_alive = True

    def __init__(self):
        self.tenants = [Tenant(input('(По умолчанию) Введите имя жильца: ')) for _ in range(2)]

    def try_cohabitation(self):
        for _ in range(365):
            if not self.is_alive:
                print('Жилец умер')
                break

            for tenant in self.tenants:
                cube = random.randint(1, 6)

                if tenant.satiety < 20:
                    tenant.do_eat()
                elif House.food < 10:
                    tenant.do_shop()
                elif House.money < 50:
                    tenant.do_work()
                elif cube == 1:
                    tenant.do_work()
                elif cube == 2:
                    tenant.do_eat()
                else:
                    tenant.do_play()
        else:
            print('Дом: \n\tЕда: {0} \n\tДеньги: {1}\n'.format(House.food, House.money))
            for i_tenant in self.tenants:
                print('{0}: \n\tСытость: {1}'.format(i_tenant.name, i_tenant.satiety, i_tenant.count))