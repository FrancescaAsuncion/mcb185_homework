# Write a function that returns the Shannon entropy for nucleotide counts a, c, g, t. 
# Demonstrate it works using multiple calls, including those where one of the counts is zero.

import math
import sys

def shannon(A, C, G, T):
	total = A + C + G + T
	assert(total>0)
	A_prob = A / total
	C_prob = C / total
	G_prob = G / total
	T_prob = T / total
	
	if A_prob <=0: sys.exit('error: porbability must be greater than 0')
	else: A_event = A_prob * math.log2(A_prob)
	if C_prob <=0: sys.exit('error: porbability must be greater than 0')
	else: C_event = C_prob * math.log2(C_prob)
	if G_prob <=0: sys.exit('error: porbability must be greater than 0')
	else: G_event = G_prob * math.log2(G_prob)
	if T_prob <=0: sys.exit('error: porbability must be greater than 0')
	else: T_event = T_prob * math.log2(T_prob)
	
	entropy = - (A_event + C_event + G_event + T_event)
	return entropy
	
print(shannon(1,2,3,4))
print(shannon(15,25,35,45))
print(shannon(0,0,1,0))