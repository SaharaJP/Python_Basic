import random

class Cell:
    def __init__(self, number):
        self.number = number
        Board.game_board[number] = ' '

class Board:
    game_board = dict()
    info_board = [num for num in range(10)]
    start_flag = False

    def __init__(self):
        for num in range(1, 10):
            Cell(num)

    def vizualization(self):
        count = 1

        if self.start_flag == False:
            board = self.info_board
            Board.start_flag = True
        else:
            board = self.game_board

        for i_line in range(3):
            for j_line in range(count, count + 2):
                print('  {0}  |'.format(board[j_line]), end = '')
            else:
                print('  {0}'.format(board[j_line + 1]))

            if i_line < 2:
                print('-' * 5 + '|' + '-' * 5 + '|' + '-' * 5)

            count += 3
        else:
            print()

class Player:
    def __init__(self, name):
        self.name = name

    def side_choice(self):
        if int(input('За какую сторону будете играть?\n'
                     '(За нолики - 0, За крестики - 1) ')) == 1:
            return 'x', 'o'
        else:
            return 'o', 'x'

    def make_a_move(self, sign):
        while True:
            try:
                move = int(input('\nВаш ход. \nНапишите, куда поставить знак: '))

                if Board.game_board[move] ==  ' ':
                    Board.game_board[move] = sign
                    break
                else:
                    print('Эта клетка уже занята, выберите другую')

            except ValueError:
                print('Вы не указали место, куда поставить знак, попробуйте еще раз')

class Bot:
    def bot_make_a_move(self, sign):
        while True:
            move = random.randint(1, 9)

            if Board.game_board[move] ==  ' ':
                Board.game_board[move] = sign
                break
            else:
                continue

class Win(Exception):
    def __init__(self, text):
        self.text = text

class Tic_tac_toe:
    def __init__(self):
        self.board = Board()
        self.player = Player('a')
        self.bot = Bot()

    def game_info(self):
        print('Перед началом игры просмотрите на номера клеток\n'
              'Это понадобится вам для понимания, куда поставить свой знак\n')
        self.board.vizualization()

    def game_rules(self):
        if input('Вы знакомы с правилами игры в крестики-нолики? (Y/N) ').lower() == 'y':
            return
        else:
            print('\nИгроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики).\n'
                  'Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.\n'
                  'Первый ход делает игрок, ставящий крестики.\n'
                  '\nПример выигранной партии в крестики-нолики:')
            print('     |     |  x  \n'
                  '-----|-----|-----\n'
                  '  o  |  o  |  x  \n'
                  '-----|-----|-----\n'
                  '  x  |  o  |  x  ')

    def start_game(self):
        if input('\nВы готовы начать игру? (Y/N) ') == 'y':
            return
        else:
            if input('Хотите еще раз просмотреть информацию о номерах клеток '
                     'или правила игры? (Y/N) ') == 'y':
                self.game_info()
                self.game_rules()
                self.start_game()
            else:
                self.start_game()

    def is_end(self):
        try:
            count = 1
            for _ in range(3):
                if (Board.game_board[count] == 'x' and Board.game_board[count + 1] == 'x' and Board.game_board[count + 2] == 'x'):
                    raise Win('Крестики победили!')
                elif (Board.game_board[count] == 'o' and Board.game_board[count + 1] == 'o' and Board.game_board[count + 2] == 'o'):
                    raise Win('Нолики победили!')
                count += 3

            for i in range(1, 4):
                if (Board.game_board[i] == 'x' and Board.game_board[i + 3] == 'x' and Board.game_board[i + 6] == 'x'):
                    raise Win('Крестики победили!')
                elif (Board.game_board[i] == 'o' and Board.game_board[i + 3] == 'o' and Board.game_board[i + 6] == 'o'):
                    raise Win('Нолики победили!')

            if (Board.game_board[1] == 'x' and Board.game_board[5] == 'x' and Board.game_board[9] == 'x'):
                raise Win('Крестики победили!')
            elif (Board.game_board[1] == 'o' and Board.game_board[5] == 'o' and Board.game_board[9] == 'o'):
                raise Win('Нолики победили!')

            if (Board.game_board[3] == 'x' and Board.game_board[5] == 'x' and Board.game_board[7] == 'x'):
                raise Win('Крестики победили!')
            elif (Board.game_board[3] == 'o' and Board.game_board[5] == 'o' and Board.game_board[7] == 'o'):
                raise Win('Нолики победили!')

        except Win:
            raise Win('Спасибо за игру!')

    def game(self):
        self.game_info()
        self.game_rules()

        self.start_game()

        player, bot = self.player.side_choice()

        if player == 'o':
            self.bot.bot_make_a_move(bot)
            self.board.vizualization()
            self.is_end()

        game_count = 0
        while True:
            game_count += 2
            self.player.make_a_move(player)
            self.board.vizualization()
            self.is_end()

            if game_count >= 9:
                break

            self.bot.bot_make_a_move(bot)
            self.board.vizualization()
            self.is_end()

        print('Ничья! \nСпасибо за игру!')





a = Tic_tac_toe()
a.game()