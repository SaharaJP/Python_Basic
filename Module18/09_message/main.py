message = input('Сообщение: ').split()
result = ''

new_message = [list(word[::-1])
               for word in message
               ]

for r_word in new_message:
    for sym in r_word:

        if not sym.isalpha():
            r_word.insert(len(r_word[r_word.index(sym):]) , sym)
            r_word.remove(r_word[r_word.index(sym)])
            break

    r_word = ''.join(r_word)
    result += r_word + ' '

print(result)