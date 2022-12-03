def syntax_error():
    correct = input('Обнаружена ошибка в строке: {0}  Хотите исправить? '.format(line)).lower()

    if correct == 'да':
        new_line = input('Введите исправленную строку: ')
        res_sum[0] += eval(new_line)


res_sum = [0]

with open('calc.txt', 'r') as calc:
    for line in calc.read().split('\n'):

        try:
            for sym in {'+', '-', '*', '/', '//', '%'}:
                if sym in line:
                    res_sum[0] += eval(line)
                    break
            else:
                raise SyntaxError

        except SyntaxError:
            syntax_error()

    print('Сумма результатов:', res_sum)