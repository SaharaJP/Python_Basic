class Warrior:
    warrior_count = 0
    warriors = {}

    def __init__(self):
        Warrior.warrior_count += 1
        Warrior.warriors[self.warrior_count] = 100