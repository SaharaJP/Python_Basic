import random

class Student:

    def __init__(self, name, group, mark = 0, average_mark = 0):
        self.name = name
        self.group = group
        self.mark = [random.randint(2, 5) for _ in range(5)]
        self.average_mark = sum(self.mark) / len(self.mark)

    def print_info(self):
        print('ФИ: {0}, Номер группы: {1}, Успеваемость: {2}, Средний балл: {3}'.format(
            self.name, self.group, self.mark, self.average_mark
        ))