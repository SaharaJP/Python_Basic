import random

class Child:

    def __init__(self, name, parent_age):
        self.name = name
        self.age = random.randint(1, parent_age - 16)
        self.are_hungry = random.randint(0, 1)
        self.are_calm = random.randint(0, 1)

    def hunger(self):
        if self.are_hungry == 1:
            return True
        else:
            return False

    def calm(self):
        if self.are_calm == 1:
            return True
        else:
            return False

class Parent:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = [Child(c_name, age) for c_name in children]

    def child_hunger(self):
        for child in self.children:
            if child.hunger():
                print('{0} не голоден'.format(child.name))
            else:
                print('{0} голоден'.format(child.name))
                child.hunger() == 1

    def child_calm(self):
        for child in self.children:
            if child.calm():
                print('{0} спокоен'.format(child.name))
            else:
                print('{0} не спокоен'.format(child.name))

    def print_info(self):
        print('\nИмя родителя: {0} \nВозраст родителя: {1}'.format(
            self.name, self.age
        ))

        for child in self.children:
            print('\nИмя ребенка: {0} \nВозраст: {1}'.format(
                child.name, child.age
            ))


a = Parent('Nik', 50, ['Sam', 'Pam'])
a.child_hunger()
a.child_calm()
a.print_info()