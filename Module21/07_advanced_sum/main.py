def summ(*args, res = [0]):
    for i_el in args:

        if not isinstance(i_el, int):
            for j_el in i_el:
                result = summ(j_el)

        else:
            res[0] += i_el

    return res[0]

# print(summ(1, 2, 3, 4, 5))