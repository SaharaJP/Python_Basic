def my_zip(a, b):

    a, b= tuple(a), tuple(b)

    result = [
        (a[i], b[i])
        for i in range(min(len(a), len(b)))
    ]

    return result


a = [{"x": 4}, "b", "z", "d"]

b = (10, {20,}, [30], "z")

print(my_zip(a, b))
