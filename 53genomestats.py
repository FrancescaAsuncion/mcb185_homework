"""
Write a program that reads a GFF file and reports the following information about the length 
of GFF features.

count
min
max
mean
standard deviation
median
Run your program on the GFF files for the A.thaliana, C.elegans, and D.melanogaster genomes. 
You will find the files in the MCB185 data directory.

Use sys.argv to specify the path to the GFF and the type of feature. 
This will allow you to write the program once and change command line parameters for 
different files or feature types.
"""

import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]


lengths = []

with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] == feature:
			beg = int(words[3])
			end = int(words[4])
			lengths.append(end - beg + 1)
	
#count
def counts(vals):
	counts = 0
	for val in vals:
		counts += 1
	return counts
print('count:', counts(lengths))

#min
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		return mini
print('minimum:', minimum(lengths))


#max
def maximum(vals):
	maxi = vals[0]
	for val in vals[1:]:
		if val > maxi: maxi = val
	return maxi
print('maximum:', maximum(lengths))

#mean
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
print('mean:', mean(lengths))

#sd
def sd(vals):
	amt = counts(vals)
	total = 0
	x = 0
	
	for val in vals:
		total += val
	mean_val = total / amt
	
	for val in vals: x += (val - mean_val) ** 2
	return(x / amt) ** 0.5
print('standard deviation:', sd(lengths))

#median
def median(vals):
	vals.sort()
	nt = len(vals)
	middle = nt // 2
	
	if nt % 2 == 0:
		med = (vals[middle - 1] + vals[middle] / 2)
	else: med = vals[middle]
	return med
print('med:', median(lengths))
	

	
