

import sys
import mcb185
"""
#retrieves next record from FASTA file, window this
k = 3
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	pro = []
	print(defline, seq[:30])
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		print(codon)
	#print(defline[:30], seq[:40], len(seq))
	
#program that calculates GC comp of nucleotide seq in fasta file
k = 3
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split() #19/20 splits and assign unique identifier to a variable called name
	name = defwords[0]
	gc = 0
	for nt in seq: #if C or G, count them
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
	
# counts 5 nu, not just Cs and Gs
k = 3
for defline, seq in mcb185.read_fasta(sys.argv[1]):
A = 0
C = 0
G = 0
T = 0
N = 0
for nt in seq:
	if nt == 'A': A += 1
	elif nt == 'C': C += 1
	elif nt == 'G': G += 1
	elif nt == 'T': T += 1
	else: N += 1
print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
"""
import sys
import mcb185

nts = 'ACGTN'
counts = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):

for i in range(len(nts)): counts.append(0)

for nt in seq:
	if nt == 'A': counts[0] += 1
	elif nt == 'C': counts[1] += 1
	elif nt == 'G': counts[2] += 1
	elif nt == 'T': counts[3] += 1
	else: counts[4] += 1
	
print(name, end='\t')
for n in counts: print(f'{n/len(seq):.4f}', end='\t')
print()