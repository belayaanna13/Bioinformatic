import time
import random
import math

#Вычисляет индекс, куда засунуть число x
def Hash_function(b):
    return (b*10)//1




m = [0, 1]
c = 2
n = 0 #количество чисел в массиве
time_arr = []
n_arr = []

hash_table = {
    0:[],
    1:[],
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[],
    8:[],
    9:[]
}
k = 0

for i in range(1000):
    n+= 1
    x = random.random()
    a = random.random()  # число, добавляемое в таблицу
    if n >= 167:
        x = a

    hash_table[Hash_function(a)].append(a)

    time_from_start = time.time()
    for i in hash_table[x*10//1]:
        if x == i:
            k = 1
            break

    # if k == 1:
    #     print(f'Число {x} найдено в массиве {arr}')
    # else:
    #     print(f'Число {x} не найдено в массиве {arr}')
    time_of_program = time.time() - time_from_start

    n_arr.append(n)
    time_arr.append(time_of_program)

average = round((sum(time_arr)/len(n_arr)), 2)
#
# print(average)

average_time = []
average_time.append(average)
print(time_arr)
print(n_arr)

import numpy as np
import matplotlib.pyplot as plt

x = np.array(time_arr)
y = np.array(n_arr)
fig, ax = plt.subplots()
ax.scatter(x, y, c = '#FFE2B7')
ax.set_facecolor('black')
fig.set(figwidth = 8,
figheight = 8)



# fig = plt.subplots()
# y = lambda x: x
# x = np.linspace(0, 1, 10000)
# plt.plot(x, y(x))
# plt.show()

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({'Time': [time_of_program],
#                    'n': [n]
# })


#Способ_1
# df.to_excel('task.xlsx')
# np.savetxt('task.xlsx', df)

#Способ_2
# sheet = 'Лист1'
# df.reset_index(level=0, inplace=True)
# with pd.ExcelWriter('./task.xlsx') as writer:
#     df.to_excel(writer, sheet_name = sheet, header=None, index=None)



