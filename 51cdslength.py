#51cdslength.py

import gzip
lengths = []
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue #resets loop at next line
		words = line.split() #splits @ any space
		if words[2] != 'CDS': continue #we only want CDS
		beg = int(words[3]) #turns strings into integers of 3rd column
		end = int(words[4]) #4th column, bc we split it by space already
		print(end - beg + 1)