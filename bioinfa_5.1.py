from Bio.Align import PairwiseAligner

aligner = PairwiseAligner()
aligner.mode = 'global'
aligner.match_score = 5
aligner.mismatch_score = -4
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5

alignments = aligner.align()

print(alignments[0])

