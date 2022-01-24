import time

time_from_start = time.time()

m = [0, 1]
c = 2
n = 5 #количество чисел в массиве
x = 0.137
arr = [0.11, 0.137, 0.367, 0.872, 0.987]

hash_table = {
    0:[],
    1:[0.11, 0.137],
    2:[],
    3:[0.3112, 0.367, 0.387, 0.395],
    4:[],
    5:[],
    6:[],
    7:[],
    8:[0.872],
    9:[0.987]
}
c = 0

for i in hash_table[x*10//1]:
    if x == i:
        c = 1
        break

if c == 1:
    print(f'Число {x} найдено в массиве {arr}')
else:
    print(f'Число {x} не найдено в массиве {arr}')

time_of_program = time.time() - time_from_start
print(time_of_program)

import pandas as pd
import numpy as np

df = pd.DataFrame({'Time': [time_of_program],
                   'n': [n]
})


#Способ_1
df.to_excel('./task.xlsx')
np.savetxt('./task.xlsx', df)

#Способ_2
# sheet = 'Лист1'
# df.reset_index(level=0, inplace=True)
# with pd.ExcelWriter('./task.xlsx') as writer:
#     df.to_excel(writer, sheet_name = sheet, header=None, index=None)



