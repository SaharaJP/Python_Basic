import random

class Warior:
    warior_count = 0
    wariors = {}

    def __init__(self):
        Warior.warior_count += 1
        Warior.wariors[self.warior_count] = 100


class Fight:
    for _ in range(2):
        Warior()

    while True:
        attack = random.randint(1, Warior.warior_count)

        if attack == 1:
            defence = 2
        else:
            defence = 1

        Warior.wariors[defence] -= 20

        print('Воин {0} наносит удар воину {1}. \n'
              'У воина {1} осталось {2} очков здоровья\n'.format(
            attack, defence, Warior.wariors[defence]))

        if Warior.wariors[defence] == 0:
            print('Воин {0}, пал от руки воина {1}'.format(
                defence, attack))
            break