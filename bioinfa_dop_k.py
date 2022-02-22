from Bio import SeqIO
from time import time

k = int(input('Введите k: '))
set_ = set()
ind = 0

t = time()

sequence = SeqIO.parse('D:\\GRCh38_latest_genomic.fna\GRCh38_latest_genomic.fna', 'fasta')

for l in sequence:
    if len(set_) == 4**k:
        break
    i = l.seq.upper()
    for j in range(len(i)):
        if j == len(i) - k + 1:
            break
        if i[j] != 'N' and i[j + k - 1] != 'N':
            if i[j:j + k] not in set_:
                set_.add(i[j:j + k])
                print(len(set_))
        if len(set_) == 4**k:
            break

if len(set_) == 4**k:
    print('Не то k')
else:
    print('То k')

print(time() - t)

# letters = ['A', 'G', 'C', 'T']
# avail_var = letters
# avg_list = []
#
# if k > 1:
#     for i in range(k-1):
#         for letter in letters:
#             for l in avail_var:
#                 avg_list.append(letter + l)
#         avail_var = avg_list
#         avg_list = []
