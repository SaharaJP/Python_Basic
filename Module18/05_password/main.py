while True:
    password = list(input('Введите пароль: '))
    upper_letters_count = len(
                            [letter for letter in password
                            if letter.isupper()]
                              )
    cyfer_count = len(
                    [num for num in password
                    if num.isdigit()]
                      )

    if upper_letters_count >= 1 and cyfer_count >= 3:
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадеждный. Попробуйте еще раз.')