n = int(input())
m = 0

for i in range(n):
    number = int(input())
    if number > 0 and number % 17 == 0 and number % 2 == 0:
        m += 1
print(f'Количество искомых чисел: {m}')