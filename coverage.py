import sys
import random

csize = int(sys.argv[1])
rsize = int(sys.argv[2])
rnum = int(sys.argv[3])

#create an empty chromosome
chrom = []
for i in range(csize): chrom.append(0) #however big the chromosome is csize
#print(chrom)
	
#fill chrom with reads, don't make a new variable unless its in the previous loop
for i in range(rnum):
	pos = random.randint(0, csize - rsize)
	for j in range(rsize):	
		chrom[pos + j] += 1 #at this position @ j, go up one
print(chrom)

#min coverage - min value across line (we know its gonna be at the ends so we need to skip those and look at middle)
min = rnum 
for n in chrom[rsize:-rsize]:
	if n < min: min = n
print(min)

#window
k = 15 #how many letters
seq = 'AGCTCGTAGCATGCAGTCAGTGCACAC'
for i in range(0, len(seq) - k + 1, 1): #skip by 3 if to turn into translation
	win = seq[i:i+k]
	g = win.count('G')
	c = win.count('C')
	print(i, win, (c + g)/k)
	#print(win)
	#print(seq[i:i+k]) 

"""
for i in range(0, csize-rsize + 1):  #without rsize + 1 you go beyond window and get a short output
	print(chrom[i:i + rsize])
"""