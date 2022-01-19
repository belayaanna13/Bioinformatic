x = float(input('Введите число "x": '))
count = 0
while 1:
    vvod = input()
    if vvod == 'Stop':
        break
    elif x == float(vvod):
        count += 1

print(f'Число вхождений числа "x": {count}')
