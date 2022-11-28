def error_messgs(line):
    if not len(line) == 3:
        raise IndexError

    if not line[0].isalpha():
        raise NameError

    if not '@' and '.' in line[1]:
        raise SyntaxError

    if not 10 <= int(line[2]) <= 99:
        raise ValueError


with open('registrations.txt', 'r', encoding = 'utf-8') as file:

    good_log = open('registrations_good.log.txt', 'w', encoding = 'utf-8')
    bad_log = open('registrations_bad.log.txt', 'w', encoding = 'utf-8')

    for line in file.read().split('\n'):
        try:
            error_messgs(line.split())
            good_log.write(line + '\n')

        except IndexError:
            bad_log.write('{0} \t\t НЕ присутствуют все три поля\n'.format(line))

        except NameError:
            bad_log.write('{0} \t\t Поле «Имя» содержит НЕ только буквы\n'.format(line))

        except SyntaxError:
            bad_log.write('{0} \t\t Поле «Имейл» НЕ содержит @ и . (точку)\n'.format(line))

        except ValueError:
            bad_log.write('{0} \t\t Поле «Возраст» НЕ является числом от 10 до 99\n'.format(line))

    good_log.close()
    bad_log.close()