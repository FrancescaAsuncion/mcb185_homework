
#Write a function that solves the quadratic formula (ax^2 + bx + c), returning the two X-intercepts. 
#Demonstrate that it works by using the formula multiple times within the program.

import math
def quadratic_formula(a, b, c):
	roots = math.sqrt(b**2 - 4*a*c)
	square_1 = (-b + roots) / (2*a)
	square_2 = (-b - roots) / (2*a)
	return roots, square_1, square_2
print(quadratic_formula(2,3,8))