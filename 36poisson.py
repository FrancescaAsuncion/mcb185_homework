"""
Create a function that computes the Poisson probability of k 
events occuring with an expectation of n: n^k e^-n / k! and 
demonstrate it works by calling it with several values of n and k. Use math.e.
"""
#done

import math

def poisson(n, k):
	formula = ((n ** k) * (math.e ** -n)) / math.factorial(k)
	return formula
	
print(poisson(20, 15))
print(poisson(10,14))
print(poisson(35,12))
