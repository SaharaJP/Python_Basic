import os

zen = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
zen_text = open(zen, 'r')

sym_dict = dict()
sym_count = 0
word_count = 0
line_count = 0

for line in zen_text:
    line_count += 1
    word_count += len(line.split())

    for sym in line:
        if sym.isalpha():
            sym_count += 1

            if sym.lower() in sym_dict:
                sym_dict[sym.lower()] += line.count(sym.lower())
            else:
                sym_dict[sym.lower()] = line.count(sym.lower())

zen_text.close()

for i_key in sym_dict.keys():
    if sym_dict[i_key] == min(sym_dict.values()):
        min_sym = i_key
        break

print('Количество букв в файле:', sym_count)
print('Количество слов файле:', word_count)
print('Количество строк в файле', line_count)
print('Наиболее редкая буква', min_sym)