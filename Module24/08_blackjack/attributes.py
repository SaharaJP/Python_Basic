import random

class Card:

    def __init__(self, suit):
        Deck.full_deck[suit] = {
                0: [value for value in range(2, 11)],
                1: [10],
                2: [10],
                3: [10],
                4: [11]
            }


class Deck:
    full_deck = dict()

    def deck_initialize(self):
        for suit in range(4):
            Card(suit)


class Player:
    player_hand = list()
    count = 0
    total_value = 0

    def __init__(self, name):
        self.name = name

    def generate_random(self):
        suit = random.randint(0, 3)
        character = random.randint(0, 4)
        available_lenght = len(Deck.full_deck[suit][character])

        return suit, character, available_lenght

    def get_card_value(self):
        suit, character, available_lenght = self.generate_random()

        try:
            if available_lenght > 1:
                card_value = Deck.full_deck[suit][character].pop(random.randint(0, available_lenght))
            elif available_lenght == 1:
                card_value = Deck.full_deck[suit][character].pop()
            elif available_lenght == 0:
                card_value = self.get_card_value()
                return card_value
        except IndexError:
            card_value = Deck.full_deck[suit][character].pop(random.randint(0, available_lenght))

        if (card_value == 11) and (self.total_value + card_value > 21):
            return suit, character, 1

        return suit, character, card_value

    def card_distribution(self):
        if self.count == 0:
            cards_count = 2
            Player.count += 1
        else:
            cards_count = 1

        for _ in range(cards_count):
            suit, character, card_value = self.get_card_value()
            Player.total_value += card_value

            for card in Player.player_hand:
                if Player.total_value > 21 and card[2] == 11:
                    Player.total_value -= card_value
                    card[2] = 1

            self.player_hand.append([suit, character, card_value])


class Dealer:
    dealer_hand = list()
    total_value = 0

    def generate_random(self):
        suit = random.randint(0, 3)
        character = random.randint(0, 4)
        available_lenght = len(Deck.full_deck[suit][character])

        return suit, character, available_lenght

    def get_card_value(self):
        suit, character, available_lenght = self.generate_random()

        try:
            if available_lenght > 1:
                card_value = Deck.full_deck[suit][character].pop(random.randint(0, available_lenght))
            elif available_lenght == 1:
                card_value = Deck.full_deck[suit][character].pop()
            elif available_lenght == 0:
                card_value = self.get_card_value()
                return card_value
        except IndexError:
            card_value = Deck.full_deck[suit][character].pop(random.randint(0, available_lenght))

        if (card_value == 11) and (self.total_value + card_value > 21):
            return suit, character, 1

        return suit, character, card_value

    def card_distribution(self):
        for _ in range(2):
            suit, character, card_value = self.get_card_value()
            Dealer.total_value += card_value

            self.dealer_hand.append([suit, character, card_value])