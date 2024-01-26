# Write a program that returns the oligo melting temperature given the number of As, Cs, Gs, and Ts in the oligo. Use these two methods.
# For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
# For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)
# Demonstrate that your program works by computing the Tm of several oligos of different sizes.

import math

def oligos(A,C,G,T):
	o_length = A + C + G + T
	if o_length <= 13:
		Tm = (A + T) * 2 + (G + C) * 4
		return Tm
	else:
		Tm = 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)
		return Tm
print(oligos(10,10,10,10))
print(oligos(20,20,20,20))
print(oligos(2,2,2,2))