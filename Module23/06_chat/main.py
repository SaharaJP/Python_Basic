def message_body():
    if count[0] < 1:
        chat_w.write('\n' + name + '\n')
        count[0] += 1

    chat_w.write('<' + ('-' * (len(message) + 2)) + '>' + '\n')
    chat_w.write('| ' + message + ' |' + '\n')
    chat_w.write('<' + ('-' * (len(message) + 2)) + '>' + '\n')

def read_message():
    interuct = False
    for line in chat_r.read().split('\n'):
        if name == line.split(' ')[-1]:
            interuct = True

        if interuct == True:
            print(' ' * (40 - len(line)) + line)
            if line == '':
                interuct = False

        else:
            print(line)


name = input('Здравствуйте! Введите ваше имя: ')
count = [0]

while True:
    choice = int(input('Выберите действие:\n'
                   '1. Посмотреть текущий текст чата.\n'
                   '2. Отправить сообщение\n'))

    if choice == 1:
        chat_r = open('chat.txt', 'r', encoding = 'utf-8')
        read_message()

        chat_r.close()

    elif choice == 2:
        chat_w = open('chat.txt', 'a', encoding='utf-8')

        message = input('Введите сообщение: ')
        message_body()

        chat_w.close()

    else:
        print('Неизвестная команда, попробуйте еще раз.')