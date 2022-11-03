zen = open('zen.txt', 'r')

count = zen.read().count('\n')

for num in range(1, count + 2):
    zen.seek(0)
    line = zen.readlines()[-num]

    if line.endswith('\n'):
        line = line.replace('\n', '')

    print(line)

zen.close()