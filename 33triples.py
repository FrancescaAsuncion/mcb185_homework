# Write a program that finds all Pythagorean triples for triangles with sides a and b less than 100. 
# For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. 
# Hint: all sides, including the hypotenuse, must be an integer.



import math

for a in range(1,100):
	for b in range(1,100):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0:
			print(a, b, round(c))

	