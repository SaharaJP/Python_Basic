def text_info_input():
    text = open('text.txt', 'w')
    text.write('Mama myla ramu.')
    text.close()

def analysis_info_input():
    text = open('text.txt', 'r')
    analysis = open('analysis.txt', 'w')

    word_dict = dict()
    sym_count = 0

    for sym in text.read().lower():
        if sym.isalpha():
            sym_count += 1

            if sym in word_dict:
                word_dict[sym] += 1
            else:
                word_dict[sym] = 1

    for i_key, i_value in word_dict.items():
        sym_calc = round((i_value / sym_count), 3)
        analysis.write('{0} {1}'.format(i_key, sym_calc) + '\n')

    text.close()
    analysis.close()

def info_output():
    text = open('text.txt', 'r')
    analysis = open('analysis.txt', 'r')

    print('Cодержимое файла {0}'.format('text.txt'))
    print(text.read())
    text.close()

    print('\nCодержимое файла {0}'.format('analysis.txt'))
    print(analysis.read())
    analysis.close()


text_info_input()
analysis_info_input()
info_output()