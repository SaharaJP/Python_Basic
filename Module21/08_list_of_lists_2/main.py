def summ(*args):
    for i_el in args:
        if isinstance(i_el, int):
            return i_el

        for j_el in i_el:
            result = summ(j_el)
            if result:
                res.append(result)



nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
res = []
summ(nice_list)

print('Ответ:', res)