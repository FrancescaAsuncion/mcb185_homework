"""
Create a program that generates DNA sequences in FASTA format. 
There should be a variable that controls how many sequences (e.g. 3). 
Each sequence should have a unique identifier (e.g. seq-1) and the 
length of the sequence should have some random range (e.g 50-60). 
The output should resemble the example below.

>seq-1
GCCGTCTCGGGGGAGAACGAGCGACTGCTGTCCCGGGATGTGCGTAAATGCGGGC
>seq-2
GGTTTTAATAGCACCCGAAGCTCCATCCAGCTAGACGTCGAAGCTTTTTAACACTGTA
>seq-3
CAGTATGGTCCACCCGCCTTTCAGGAATACTTCATCCTAAGTGCCTCGAA
"""


import random
for i in range(3):
	print(f'>seq-{i + 1}')
	for dna in range(random.randint(50, 60)):
		print(random.choice('ATCG'), end='')
	print()
		

