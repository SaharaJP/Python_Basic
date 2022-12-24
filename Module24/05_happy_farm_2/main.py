class Potato:
    states = {0 : 'Отсутствует', 1 : 'Росток', 2 : 'Зеленая', 3 : 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {0} сейчас {1}'.format(
            self.index, Potato.states[self.state]
        ))

class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка проростает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            return True
        else:
            return False

class Gardener:
    garden_count = 0
    bag = {}

    def __init__(self, name, potato_index):
        self.potato_index = potato_index
        self.name = name
        self.garden = PotatoGarden(potato_index)

    def garden_care(self):
        while self.garden.are_all_ripe():
            self.garden.grow_all()
        else:
            print('Вся картошка созрела, можно собирать!\n')

    def collect(self):
        if not self.garden.are_all_ripe():
            Gardener.garden_count += 1
            self.bag[self.garden_count] = self.potato_index
        else:
            print('Картошка еще не созрела!\n')

        for garden, collected in self.bag.items():
            print('Урожай с {0}-й грядки: {1} картошек'.format(garden, collected))


b = Gardener('Andrew', 5)
b.collect()
b.garden_care()
b.collect()

c = Gardener('Andrew', 7)
c.garden_care()
c.collect()