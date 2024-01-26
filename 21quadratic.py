"""
Write a function that solves the quadratic formula (ax^2 + bx + c), returning the two X-intercepts. 
Demonstrate that it works by using the formula multiple times within the program.

"""
import math
def quadratic_formula(a, b, c):
	roots = math.sqrt(b**2 - 4*a*c)
	b1 = (-b + roots) / (2*a)
	b2 = (-b - roots) / (2*a)
	return b1
	return b2
quadratic = quadratic_formula(a, b, c)
print(quadratic)