from math import inf

n = int(input('Введите количество чисел в массиве: '))
m_1 = float(input('Введите число из массива: '))
m_2 = float(input('Введите число из массива: '))
k = 0

if m_2 > m_1:
    a = m_1
    m_1 = m_2
    m_2 = a
elif m_2 == m_1:
  m_2 = - inf

for i in range(n-2):
    number = float(input('Введите число из массива: '))

    if k == 0:
        if number > m_1:
            m_3, m_2, m_1 = m_2, m_1, number
        elif number < m_1 and number > m_2:
            m_3, m_2, = m_2, number
        elif number < m_2:
            m_3 = number
        else:
            m_3 = - inf
    else:
        if number > m_1:
            m_3, m_2, m_1 = m_2, m_1, number
        elif number < m_1 and number > m_2:
            m_3, m_2 = m_2, number
        elif number < m_2 and number > m_3:
            m_3 = number

    k += 1
print(f'Искомое число: {m_3}')