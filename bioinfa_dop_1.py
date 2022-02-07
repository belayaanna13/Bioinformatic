f_seq = list(input('Введите последовательность: '))
s_seq = list(input('Введите последовательность: '))

table_A = []
table_B = []
table_S = []

d = 10
match = 5
dismatch = -4

def s(i, j):
    if f_seq[i-1] == s_seq[j-1]:
        return match
    else:
        return dismatch

#записываем первые столбец и строку таблицы S
ap_d = 0
ap_d_ = -10
for i in range(len(f_seq)+1):
    table_S.append([ap_d])
    if ap_d == 0:
        ap_d -= 10
    else:
        ap_d -= 0.5
    if i == 0:
        for j in range(len(s_seq)):
            table_S[i].append(ap_d_)
            ap_d_ -= 0.5

#записываем первую строку таблицы А
first_n = table_S[0][1] - 10

for i in range(len(f_seq)):
    table_A.append([])
    if i == 0:
        for j in range(len(s_seq)):
            table_A[i].append(first_n)
            first_n -= 0.5

#записываем первую строку таблицы B
first_n = table_S[1][0] - 10

for i in range(len(f_seq)):
    table_B.append([])
    for j in range(len(f_seq)):
        if j == 0:
            table_B[i].append(first_n)
            first_n -= 0.5

for i in range(1, len(f_seq)+1):

    # print(table_A)
    for j in range(1, len(s_seq)+1):
        # start_B = table_B[i - 1][j - 1]
        if j != 1:
            start_B = max(table_S[i][j-1] - d, table_B[i-1][j-2] - 0.5)
            table_B[i - 1].append(start_B)
        elif j == 1:
            start_B = table_B[i-1][0]
        max_number = max(table_S[i-1][j-1] + s(i,j), start_B, table_A[i-1][j-1])
        table_S[i].append(max_number)
        # table_S[i].append(max_number)
        # print(table_S)

    # заполняем строку таблицы А
    for k in range(len(s_seq)):
        if i != len(f_seq):
            if table_A[i-1][k] - 0.5 <= table_S[i][k+1] - 10:
                table_A[i].append(table_S[i][k+1] - 10)
            elif table_A[i-1][k] - 0.5 >= table_S[i][k+1] - 10:
                table_A[i].append(table_A[i-1][k] - 0.5)
# for i in table_S:
#     print(i)

f_seq_new = []
s_seq_new = []

i = len(f_seq)
j = len(s_seq)

while 1:
    if i == 0 and j == 0:
        break
    last_number = table_S[i][j]
    if last_number == table_S[i-1][j-1] + s(i,j):
        f_seq_new.append(f_seq[i-1])
        s_seq_new.append(s_seq[j-1])
        i -= 1
        j -= 1
    elif last_number == table_A[i-1][j-1]:
        s_seq_new.append('-')
        f_seq_new.append(f_seq[i-1])
        i -= 1
    elif last_number == table_B[i-1][j-1]:
        f_seq_new.append('-')
        s_seq_new.append(s_seq[j-1])
        j -= 1
f_seq_new.reverse()
s_seq_new.reverse()

av = []
for i in range(len(f_seq_new)):
    if f_seq_new[i] == s_seq_new[i]:
        av.append('|')
    elif f_seq_new[i] == '-' or s_seq_new[i] == '-':
        av.append(' ')
    else:
        av.append('.')

print(''.join(f_seq_new))
print(''.join(av))
print(''.join(s_seq_new))

print(f'SCORE: {table_S[-1][-1]}')