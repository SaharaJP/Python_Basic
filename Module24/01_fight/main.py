import random
from warrior import Warrior

def fight():
    for _ in range(2):
        Warrior()

    while True:
        attack = random.randint(1, Warrior.warrior_count)

        if attack == 1:
            defence = 2
        else:
            defence = 1

        Warrior.warriors[defence] -= 20

        print('Воин {0} наносит удар воину {1}. \n'
              'У воина {1} осталось {2} очков здоровья\n'.format(
            attack, defence, Warrior.warriors[defence]))

        if Warrior.warriors[defence] == 0:
            print('Воин {0}, пал от руки воина {1}'.format(
                defence, attack))
            break

battle = fight()