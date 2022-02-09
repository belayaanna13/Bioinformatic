from math import inf

# f_seq = list(input('Введите последовательность: '))
# s_seq = list(input('Введите последовательность: '))
f_seq = list('ATCAGTC')
s_seq = list('ATCCGAGTT')

fin_f_seq = []
fin_sec_seq = []

d = 10
match = 5
dismatch = -4

def s(j, i):
    if f_seq[j - 1] == s_seq[i - 1]:
        return match
    else:
        return dismatch

#находим первый результат колонки, который будет лежать в f_col:
f_col = []
s_col = []
k = 0
for i in range((len(s_seq) // 2) + 1):
    if i == 0:
        f_col.append(0)
        s_col.append(-10)
        for j in range(len(f_seq)):
            k -= 10
            f_col.append(k)
    else:
        # print(f_col)
        # print(s_col)
        for j in range(1, len(f_seq) + 1):
            n = max(f_col[j - 1] + s(j, i), f_col[j] - d, s_col[j - 1] - d)
            s_col.append(n)
            # print(s_col)

        f_col = s_col
        s_col = [-(i + 1) * 10]


k = 0
p = 2
t_col = []
four_col = []
for i in range(len(s_seq) + 2, len(s_seq) // 2 + 1, -1):
    r = len(f_seq)
    if i == len(s_seq) + 2:
        t_col.append(0)
        four_col.append(-10)
        for j in range(len(f_seq)):
            k -= 10
            t_col.append(k)
    else:
        for j in range(1, len(f_seq) + 1):
            n = max(t_col[j - 1] + s(r, i - 1), t_col[j] - d, four_col[j - 1] - d)
            r -= 1
            four_col.append(n)
            # print(s_col)

        t_col = four_col
        four_col = [-i * 10 + 10 * (i - p)]
        p += 1
t_col.reverse()

m = -inf
for i in range(len(f_col) - 1):
    if m < f_col[i + 1] + t_col[i + 1]:
        m = f_col[i + 1] + t_col[i + 1]
        max_f_col = f_col[i + 1]
        max_t_col = t_col[i + 1]
index_f = f_col.index(max_f_col)


f_seq_1 = f_seq[:index_f-1]
s_seq_1 = s_seq[:len(s_seq)//2 - 1]

f_seq_2 = f_seq[index_f:]
s_seq_2 = s_seq[len(s_seq)//2:]

fin_f_seq.append(f_seq[index_f - 1])
fin_sec_seq.append(s_seq[index_f - 1])





def hish1(f_seq, s_seq):
    f_col = []
    s_col = []
    k = 0
    for i in range((len(s_seq)//2) + 1):
        if i == 0:
            f_col.append(0)
            s_col.append(-10)
            for j in range(len(f_seq)):
                k -= 10
                f_col.append(k)
        else:
            # print(f_col)
            # print(s_col)
            for j in range(1, len(f_seq)+1):
                n = max(f_col[j-1] + s(j, i), f_col[j] - d, s_col[j-1] - d)
                s_col.append(n)
                # print(s_col)

            f_col = s_col
            s_col = [-(i+1)*10]

    k = 0
    p = 2
    t_col = []
    four_col = []
    for i in range(len(s_seq) + 2, len(s_seq) // 2 + 1, -1):
        r = len(f_seq)
        if i == len(s_seq) + 2:
            t_col.append(0)
            four_col.append(-10)
            for j in range(len(f_seq)):
                k -= 10
                t_col.append(k)
        else:
            for j in range(1, len(f_seq) + 1):
                n = max(t_col[j - 1] + s(r, i - 1), t_col[j] - d, four_col[j - 1] - d)
                r -= 1
                four_col.append(n)
                # print(s_col)

            t_col = four_col
            four_col = [-i * 10 + 10 * (i - p)]
            p += 1
    t_col.reverse()

    m = -inf
    max_f_col = 0
    for i in range(len(f_col) - 1):
        if m < f_col[i + 1] + t_col[i + 1]:
            m = f_col[i + 1] + t_col[i + 1]
            max_f_col = f_col[i + 1]
            max_t_col = t_col[i + 1]
    print(f'{f_col} : {max_f_col}')
    index_f = f_col.index(max_f_col)

    n = 0

    if len(f_seq) != 0 and len(s_seq) != 0:
        if n == 0:
            fin_f_seq.insert(0, f_seq[index_f - 1])
            fin_sec_seq.insert(0, s_seq[index_f - 1])
            n += 1
        else:
            fin_f_seq.insert(n+1, f_seq[index_f - 1])
            fin_sec_seq.insert(n+1, s_seq[index_f - 1])
            n += 1
    elif len(f_seq) == 0 and len(s_seq) != 0:
        fin_f_seq.append('-')
        fin_sec_seq.append(s_seq[:])
    elif len(f_seq) != 0 and len(s_seq) == 0:
        fin_f_seq.append(s_seq[:])
        fin_sec_seq.append('-')

    f_seq_ = f_seq
    s_seq_ = s_seq

    if len(f_seq) != 0 and len(s_seq) != 0:
        f_seq = f_seq_[:index_f-1]
        s_seq = s_seq_[:len(s_seq) // 2 - 1]
        hish1(f_seq, s_seq)

        f_seq_1 = f_seq_[index_f:]
        s_seq_1 = s_seq_[len(s_seq) // 2:]
        hish1(f_seq_1, s_seq_1)




hish1(f_seq_1, f_seq_2)
print(fin_f_seq, fin_sec_seq)