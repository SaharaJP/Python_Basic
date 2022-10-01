alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

caesar_text = text[:]
caesar_text = [(alphabet[(alphabet.index(sym) + shift) % 33]
                if sym != ' ' else ' ') for sym in caesar_text]

result = ''
for sym in caesar_text:
    result += sym

print('Зашифрованное сообщение:', result)