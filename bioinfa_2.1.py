import random as r

first_number = int(input('Введите от какого числа может быть выборка:'))
last_number = int(input('Введите до какого числа может быть выборка:'))
list = []
number = int(input('Введите число "x": '))

for i in range(int(input('Введите количество чисел в массиве:'))):
    list.append(r.randint(first_number, last_number))

print(f'Количество вхождений числа "x": {list.count(number)}')
