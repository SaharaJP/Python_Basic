def tpl_sort(exercise):
    for sym in exercise:
        if str(sym).isalpha() or not str(abs(sym)).isdigit():
            return exercise
    else:
        return tuple(sorted(exercise))

# print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))