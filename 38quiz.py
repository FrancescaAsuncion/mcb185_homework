#coauthors: Lisa Yuan, Varsha Thalladi, Anisha Patel, Avantika

def pi_calc(n):
	for i in range(1,n):
		pi = 4 * ((-1)**i / (2*i -1))
	return pi

print(pi_calc(5))

def nilakantha(iterations):
	estimate_pi = 3
	sign = 1
	
	for i in range(1, iterations):
		denominator = 2 * i * (2 * i + 1) * (2 * i + 2)
		now_add = 4 / denominator
		estimate_pi += sign * now_add
		sign *= -1
		return estimate_pi
		
for i in range(1, 100):
	print(pi_calc(i), nilakantha(i))
