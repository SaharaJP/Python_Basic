class Property:
    def __init__(self, worth = 0):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def tax(self):
        return 0

class Apartment(Property):
    def tax(self):
        return super().get_worth() / 1000

class Car(Property):
    def tax(self):
        return super().get_worth() / 200

class CountryHouse(Property):
    def tax(self):
        return super().get_worth() / 500


money = int(input('Введите сколько у вас денег?'))
apartment = Apartment(int(input('Сколько стоят апартаменты? ')))
if money < apartment.tax():
    need = apartment.tax() - money
    print('Вам не хватает {0} рублей'.format(need))

car = Car(int(input('Сколько стоит машина? ')))
if money < car.tax():
    need = car.tax() - money
    print('Вам не хватает {0} рублей'.format(need))

country_house = CountryHouse(int(input('Сколько стоит дача? ')))
if money < country_house.tax():
    need = country_house.tax() - money
    print('Вам не хватает {0} рублей'.format(need))