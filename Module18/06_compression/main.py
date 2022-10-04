text = input('Введите строку: ')
encoded_text = []
count = 1

for sym in range(len(text)):
    if text[sym] == text[sym + 1 : sym + 2]:
        count += 1
        continue
    encoded_text.append(text[sym] + str(count))
    count = 1

print('Закодированная строка: {}'.format(''.join(encoded_text)))