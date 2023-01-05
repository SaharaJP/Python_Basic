import random

karma_logs = open('karma.log.txt', 'w')

class KillError(Exception):
    def __init__(self):
        karma_logs.write('Убил\n')

class DrunkError(Exception):
    def __init__(self):
        karma_logs.write('Выпил\n')

class CarCrashError(Exception):
    def __init__(self):
        karma_logs.write('Авария\n')

class GluttonyError(Exception):
    def __init__(self):
        karma_logs.write('Обжорство\n')

class DepressionError(Exception):
    def __init__(self):
        karma_logs.write('Депрессия\n')

class Karma:
    karma = 0

    def one_day(self):
        Karma.karma += random.randint(1, 7)

        if random.randint(1, 10) == 1:
            KillError()
        elif random.randint(1, 10) == 2:
            DrunkError()
        elif random.randint(1, 10) == 3:
            CarCrashError()
        elif random.randint(1, 10) == 4:
            GluttonyError()
        elif random.randint(1, 10) == 5:
            DepressionError()


karma = Karma()
while karma.karma < 500:
    karma.one_day()

karma_logs.close()