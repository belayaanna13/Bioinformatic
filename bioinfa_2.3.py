
n = int(input('Введите количество чисел в массиве: '))
m_1 = float(input('Ввведите число из массива: '))
m_2 = float(input('Ввведите число из массива: '))
k = 0

if m_2 > m_1:
  a = m_1
  m_1 = m_2
  m_2 = a
elif m_2 == m_1:
  m_2 = None
for i in range(n-2):
        number = float(input('Ввведите число из массива: '))
        if k == 0:
            if  m_2 == None and number < m_1:
                m_2 = number
                m_3 = None
            elif m_2 == None and number > m_1:
                m_2 = m_1
                m_1 = number
                m_3 = None
            elif m_2 == None and m_1 == number:
                m_3 = None
            elif number < m_2:
                m_3 = number
            elif number > m_1:
                m_3 = m_2
                m_2 = m_1
                m_1 = number
            elif number < m_1 and number > m_2:
                m_3 = m_2
                m_2 = number
            # else:
            #     m_3 = None
        else:
            if m_3 == None and m_2 == None and number == m_1:
                m_2 = None
                m_3 = None
            elif m_2 == None and number < m_1:
                m_2 = number
            elif m_2 == None and number > m_1:
                m_2 = m_1
                m_1 = number
            elif m_3 == None and number < m_2:
                m_3 = number
            elif number < m_1 and number > m_2:
                m_3 = m_2
                m_2 = number
            elif number < m_2 and number > m_3:
                m_3 = number

            elif number > m_1:
                m_3 = m_2
                m_2 = m_1
                m_1 = number
        k += 1
print(f'Искомое число: {m_3}')


