import random

class House:
    food_count = 0
    money = 100
    food = 50
    cat_food = 30
    dirt = 0

    def __init__(self, name):
        self.__name = name
        self.satiety = 30
        self.happiness = 100

    def eat(self):
        eat = random.randint(1, 30)
        if House.food > 0:
            if House.food > eat:
                House.food_count += eat
                self.satiety += eat
                House.food -= eat
            else:
                House.food_count += House.food
                self.satiety += House.food
                House.food = 0

class Cat(House):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        eat = random.randint(1, 10)
        if House.cat_food > 0:
            if House.cat_food > eat:
                self.satiety += eat
                House.cat_food -= eat
            else:
                self.satiety += House.cat_food
                House.cat_food -= House.cat_food

    def sleep(self):
        self.satiety -= 1

    def scratching(self):
        House.dirt += 5
        self.satiety -= 1

class Wife(House):
    coat = 0

    def __init__(self, name):
        super().__init__(name)

    def buy_products(self):
        if (House.money - 20) > 0:
            House.money -= 20
            House.food += 10
            House.cat_food += 10

        self.satiety -= 1

    def shopping(self):
        if House.money > 350:
            House.money -= 350
            Wife.coat += 1
        self.satiety -= 1

    def house_cleaning(self):
        clean = random.randint(1, 100)

        if clean > House.dirt:
            House.dirt = 0
        else:
            House.dirt -= clean

        self.satiety -= 1

class Husband(House):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        House.money += 150
        self.satiety -= 1

    def play_games(self):
        if self.happiness < 80:
            self.happiness += 20
        else:
            self.happiness = 100

        self.satiety -= 1


wife = Wife('Lena')
husband = Husband('Tom')
cat = Cat('Garfield')

for _ in range(365):
    wife_todo = random.randint(1, 4)
    husband_todo = random.randint(1, 3)
    cat_todo = random.randint(1, 3)
    pet_cat = random.randint(0, 1)

    if pet_cat == 1:
        wife.happiness += 5
        husband.happiness += 5

    if House.dirt >= 90:
        wife.happiness -= 10
        husband.happiness -= 10

    if (wife.happiness or husband.happiness) <= 10:
        print('Смерть от депрессии')
        break

    if (wife.satiety or husband.satiety or cat.satiety) <= 0:
        print('Смерть от голода')
        break

    if wife_todo == 1:
        wife.eat()
    elif wife_todo == 2:
        wife.buy_products()
    elif wife_todo == 3:
        wife.shopping()
    else:
        wife.house_cleaning()

    if husband_todo == 1:
        husband.eat()
    elif husband_todo == 2:
        husband.play_games()
    else:
        husband.work()

    if cat_todo == 1:
        cat.eat()
    elif cat_todo == 2:
        cat.sleep()
    else:
        cat.scratching()

    House.dirt += 5
else:
    print('Итоги года:\n'
          'Еды съедено: {0}\n'
          'Куплено шуб: {1}'.format(
        House.food_count, wife.coat
    ))