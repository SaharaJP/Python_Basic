num = open('numbers.txt', 'r')
ans = open('answer.txt', 'w')
res = 0

for line in num:
    for el in line:
        if el.isdigit():
            res += int(el)
ans.write(str(res))

num.close()
ans.close()