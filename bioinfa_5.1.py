from Bio.Align import PairwiseAligner

from Bio import SeqIO

sequences = SeqIO.parse('SARS_Spike_NSP12.fasta', 'fasta')

k = 0
for i in sequences:
    if k == 0:
        NS_1 = i
        k+= 1
    elif k == 1:
        NS_2 = i
        k+=1
    elif k == 2:
        Sp_1 = i
        k+=1
    elif k == 3:
        Sp_2 = i
        break

aligner = PairwiseAligner()
aligner.mode = 'global'
aligner.match_score = 5
aligner.mismatch_score = -4
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5

alignments = aligner.align(NS_1.seq, NS_2.seq)

print(alignments[0])

alignments = aligner.align(Sp_1.seq, Sp_2.seq)

print(alignments[0])
