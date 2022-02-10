from Bio import SeqIO

sequences = SeqIO.parse('SARS_CoV_2_Russia_aligned.fasta', 'fasta')

spike = []
nsp12 = []
for i in sequences:
    spike.append(i.seq[21563:25384 + 1])
    nsp12.append(i.seq[13442:16236 + 1])

k = 0
mut_sp = 0
len_gene_sp = 0
for i in range(len(spike)):
    if k == 0:
        ref = spike[i]
    else:
        for j in range(len(spike[i])):
            if spike[i][j] != ref[j]:
                mut_sp += 1
        len_gene_sp += 1
    k += 1

p = 0
mut_ns = 0
len_gene_ns = 0
for i in range(len(nsp12)):
    if p == 0:
        ref = nsp12[i]
    else:
        for j in range(len(nsp12[i])):
            if nsp12[i][j] != ref[j]:
                mut_ns += 1
        len_gene_ns += 1
    p += 1

def result(count, mut, len):
    av_mut = mut/(count*len)
    return av_mut

print(f'Среднее число мутаций в Spike: {result(k, mut_sp, len_gene_sp)}')
print(f'Среднее число мутаций в NSP12: {result(p, mut_ns, len_gene_ns)}')