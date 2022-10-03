text = input('Введите строку: ').split()
most_len_word = text[0]

for word in text:
    if len(word) > len(most_len_word):
        most_len_word = word

print('Самое длинное слово:', most_len_word)
print('Длина этого слова:', len(most_len_word))