from math import inf

n = int(input('Введите количество чисел в массиве: '))
m_1 = float(input('Ввведите число из массива: '))
k = 0
for i in range(n-1):
    number = float(input('Ввведите число из массива: '))
    if k == 0:
        if number < m_1:
            m_2 = number
        elif number > m_1:
            m_2 = m_1
            m_1 = number
        else:
            m_2 = - inf
    else:
        if number < m_1 and number >= m_2:
            m_2 = number
        elif number > m_1:
            m_2 = m_1
            m_1 = number
    k += 1
print(f'Искомое число: {m_2}')









