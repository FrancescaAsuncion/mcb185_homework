#coauthors: Lisa Yuan

def pi_calc(n):
	for i in range(1,n):
		pi = 4 * ((-1)**i / (2*i -1))
	return pi

print(pi_calc(5))


