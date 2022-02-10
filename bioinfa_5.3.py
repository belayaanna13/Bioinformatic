from Bio import SeqIO

sequences = SeqIO.parse('SARS_CoV_2_Russia_aligned.fasta', 'fasta')

spike = []
for i in sequences:
    spike.append(i.seq[21563:25384 + 1])


def find_letter(A, G, T, C, max_numb):
    if max_numb == A:
        return 'a'
    elif max_numb == G:
        return 'g'
    elif max_numb == T:
        return 't'
    elif max_numb == C:
        return 'c'


name = []
max_sum = []
ref = spike[0]

for i in range(len(ref)):
    j = 1
    A = 0
    G = 0
    T = 0
    C = 0

    while j != len(spike) - 1:
        if spike[j][i] != ref[i]:
            if spike[j][i] == 'a':
                A += 1
            elif spike[j][i] == 'g':
                G += 1
            elif spike[j][i] == 't':
                T += 1
            elif spike[j][i] == 'c':
                C += 1
        j += 1
    max_numb = max(A, C, G, T)
    max_sum.append(max_numb)
    name.append(f'{ref[i]}:{find_letter(A, G, T, C, max_numb)}')

ind = max_sum.index(max(max_sum))

print(f'{name[ind]} - {max(max_sum)}')

if ind % 3 == 0:
    print(f'{ref[ind]}{ref[ind+1]}{ref[ind+2]}')
elif ind % 3 == 1:
    print(f'{ref[ind-1]}{ref[ind]}{ref[ind+1]}')
elif ind % 3 == 2:
    print(f'{ref[ind-2]}{ref[ind-1]}{ref[ind]}')





