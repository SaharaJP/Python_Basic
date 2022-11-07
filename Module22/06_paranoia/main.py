def text_file_realize():
    text_file = open('text.txt', 'a')

    for _ in range(4):
        text_file.write('Hello\n')

    text_file.close()

def text_file_cipher():
    text = open('text.txt', 'r')
    cipher_text = open('cipher_text.txt', 'a')

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 0

    for line in text.readlines():
        shift += 1

        line_cipher_dict = [(alphabet[(alphabet.index(sym) + shift) % 33]
                            if sym != '\n' else '\n')
                            for sym in line.lower()]

        line_cipher = ''.join(line_cipher_dict)
        cipher_text.write(line_cipher)

    text.close()
    cipher_text.close()


text_file_realize()
text_file_cipher()