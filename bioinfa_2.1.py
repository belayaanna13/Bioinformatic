x = float(input('Введите число "x": '))
count = 0
while 1:
    vvod = input('Введите число из массива. Если массив закончен, введите "Stop": ')
    if vvod == 'Stop':
        break
    elif x == float(vvod):
        count += 1

print(f'Число вхождений числа "x": {count}')
