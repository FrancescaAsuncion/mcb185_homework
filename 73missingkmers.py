"""
fasta = sys.argv[1]

for k in range(1, 10):
	print('checking', k)
	
	#get all kmers for all seq, create all kmers first w count 0
	kcount = {}
	
	for defline, seq in mcb185.read_fasta(fasta):
		for i in range(len(seq) - k + 1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1

	#check all kmers against all possible kmers
	if len(kcount.keys()) == 4**k: continue
	#print('missing at', k)
	
	#report missing kmers
	for ktup in itertools.product('ACGT', repeat=k):
		kmer = ''.join(ktup)
		if kmer not in kcount: print(kmer)
		
	sys.exit()
	
I know we did this in class but I accidentally put it in 72 at first and then copy and pasted it on here.
So I just re wrote the code again so there are no tabs or weird spacing bc you said it was illegal.
"""

	
import gzip
import json
import sys
import mcb185

fasta = sys.argv[1]

for k in range(1, 10):
	print('checking', k)
	
	#get all kmers for all seq, create all kmers first w count 0
	kcount = {}
	
	for defline, seq in mcb185.read_fasta(fasta):
		for i in range(len(seq) - k + 1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
			
	#check all kmers against all possible kmers
	if len(kcount,keys()) == 4**k: continue
	
	#report missing kmers
	for ktup in itertools.product('ACGT', repeat=k):
		kmer = ''.join(ktup)
		if kmer not in kcount: print(kmer)
		
	sys.exit()
			
			