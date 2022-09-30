text = input('Введите строку: ')
rev_text = text[::-1]

left = text.index('h')
right = rev_text.index('h')

if rev_text.index('h') == 0:
    i = 1
else:
    i = -1

rev_text = rev_text[- right + i : left - 1]

print('Развернутая последовательность между первым и последним h:', rev_text)