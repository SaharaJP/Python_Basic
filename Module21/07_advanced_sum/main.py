def summ(*args):
    for i_el in args:
        if isinstance(i_el, int):
            return i_el

        for j_el in i_el:
            result = summ(j_el)
            if result:
                res.append(result)


res = []
summ([[1, 2, [3]], [1], 3])
print(sum(res))