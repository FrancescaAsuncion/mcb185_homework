"""
Estimate pi using the Nilakantha series. 
Hint: you must figure out how to get the +/- to flip-flop with each iteration.

Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...

"""
iterations = 10
def nilakantha(iterations):
	pi_est = 3
	sign = 1 #switching between pos and neg
	
	for i in range(1, iterations):
		denom = 2 * i * (2 * i + 1) * (2 * i + 2)
		pi_est += sign * (4 / denom)
		sign *= -1
		return pi_est
		
nilakantha = nilakantha(iterations)		
print(nilakantha)

