from attributes import Deck, Player, Dealer

class Black_Jack:
    suits = ['Черви', 'Бубны', 'Пики', 'Трефы']
    characters = {0 : 'Цифры', 1 : 'Валет', 2 : 'Дама', 3 : 'Король', 4 : 'Туз'}

    def __init__(self):
        self.deck = Deck()
        self.deck.deck_initialize()
        self.player = Player(input('Введите имя: '))
        self.dealer = Dealer()

    def hand_info(self):
        card_count = len(self.player.player_hand)

        print('\nВ вашей руке сейчас:')

        for card in range(card_count):
            print('{0} {1} [{2}]'.format(
                self.characters[self.player.player_hand[card][1]],
                self.suits[self.player.player_hand[card][0]],
                str(self.player.player_hand[card][2])
                ))

    def is_win(self):
        if (self.player.total_value > self.dealer.total_value) and (self.player.total_value <= 21):
            print('\nВы выиграли! \nВаши очки {0} \nОчки дилера {1}'.format(
                self.player.total_value, self.dealer.total_value
            ))
        elif (self.player.total_value < self.dealer.total_value) or (self.player.total_value > 21):
            print('\nВы проиграли! \nВаши очки {0} \nОчки дилера {1}'.format(
                self.player.total_value, self.dealer.total_value
            ))
        else:
            print('\nНичья! \nВаши очки {0} \nОчки дилера {1}'.format(
                self.player.total_value, self.dealer.total_value
            ))

    def take_more_card(self):
        print('Ваша сумма равна', self.player.total_value)
        take_a_card = input('Взять еще одну карту? (Y/N) ').lower()

        if take_a_card == 'y':
            self.player.card_distribution()
            self.hand_info()
            return True
        else:
            return False

    def game(self):
        self.player.card_distribution()
        self.dealer.card_distribution()

        self.hand_info()

        while self.player.total_value < 21:
            if not self.take_more_card():
                break

        self.is_win()