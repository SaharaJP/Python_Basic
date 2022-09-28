text = list(input('Введите текст: '))
vowel_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

text_vowel_list = [vowel for vowel in text
                   if vowel in vowel_list]

print('Список гласных букв:', text_vowel_list)
print('Длина списка:', len(text_vowel_list))
