class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

class Emplyee(Person):
    def __str__(self):
        return 'Имя: {0}\n' \
               'Фамилия {1}\n' \
               'Возраст {2} \n' \
               'Величина заработной платы: {3}'.format(
            self.get_name(), self.get_surname(), self.get_age(),self.salary()
        )

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary(self):
        return 13000

class Manager(Emplyee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

class Agent(Emplyee):
    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.sales = sales

    def salary(self):
        return 5000 + self.sales / 20

class Worker(Emplyee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def salary(self):
        return 100 * self.hours
