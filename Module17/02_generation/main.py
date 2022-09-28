N = int(input('Введите длину списка: '))
result = list(range(N))
result = [1 if i % 2 == 0 else i % 5
          for i in result]
print('Резултат:', result)