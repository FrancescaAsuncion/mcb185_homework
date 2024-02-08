"""
Write a program the displays a +1/-1 scoring matrix as shown below.

   A  C  G  T
A +1 -1 -1 -1
C -1 +1 -1 -1
G -1 -1 +1 -1
T -1 -1 -1 +1
Your code must start as follows, and must be able to print a similar looking scoring matrix simply by changing the variables below.

alphabet = 'ACGT'
match = '+1'
mismatch = '-1'
Hint: use print(end=' ') to terminate print() statements with a space instead of the default newline.
"""
#done 

nts = 'ACGT'
mat = '+1'
mismatch = '-1'

#header
print(' ', end='  ')
for nt in nts:
	print(nt, end='  ')
print()


for nt in nts:
	print(nt, end=' ')
	for nt2 in nts:
		if nt == nt2:
			print(mat, end=' ')
		else:
			print(mismatch, end=' ')
	print()
