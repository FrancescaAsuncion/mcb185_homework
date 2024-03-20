"""
#53

import sys
val = []
#print(sys.argv[1:])

total = 0

for x in sys.argv[1:]: #for every item in this list in terminal after running command
	val.append(int(x))
print(val)
val.sort()
print(val)

if len(val) % 2 == 0: print('even') #even
else: print('odd')

med = val[len(val) // 2]
print(med)

 
output
python3 50demo.py 23 56 48 9 8 11 33 25 66
[23, 56, 48, 9, 8, 11, 33, 25, 66]
[8, 9, 11, 23, 25, 33, 48, 56, 66]
odd
25


import sys
val = []
#print(sys.argv[1:])

total = 0

for x in sys.argv[1:]: #for every item in this list in terminal after running command
	val.append(int(x))
print(val)
val.sort()
print(val)

if len(val) % 2 == 0:  
	med = 'idk'
else:
	med = val[len(val) // 2]
print(med)


s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:5], s[:5]) #both ABCDE
print(s[5:len(s)], s[5:]) #both FGHIJ
print(s, s[::], s[::1], s[::-1])

tax = ('Homo', 'sapiens', 9606)
print(tax)

print(tax[0]) 
print(tax[::-1])  

output:
ABCDE
ABCDE ABCDE
FGHIJ FGHIJ
ABCDEFGHIJ ABCDEFGHIJ ABCDEFGHIJ JIHGFEDCBA

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)
"""
#fxn that returns minimum value of a list
vals = [4,1,2,3,4,5,2,40,10]
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		return mini
print(minimum(vals))

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
print(minmax(vals))

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
print(mean(vals))

import math
def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))