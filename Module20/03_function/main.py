def slicer():
    new_el = int(input('Введите элемент (элемент должен являться числом): '))
    original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), new_el

    main = original_tuple[0]

    if main.count(new_el) == 0:
        return tuple()

    elif main.count(new_el) >= 2:
        return main[
               main.index(new_el) :
               main[main.index(new_el) + 1:].index(new_el) + main.index(new_el) + 2
               ]

    else:
        return main[
               main.index(new_el) :
               ]

print(slicer())