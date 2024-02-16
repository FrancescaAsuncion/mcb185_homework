"""
Write a program that estimates pi using Monte Carlo methods as was described above. 
Generate random values for x and y from 0 to 1. 
Calculate the distance to the origin. 
If the distance is less than 1, the point is inside the circle. 
The ratio of points that fall inside compared to the total is pi/4. 
Output each iteration and watch as the ratio gets closer to pi. 
Use an endless while loop in your program and stop it with ^C.

"""

import random
import math

inside = 0 
total = 0 

while True:
	x = random.random()
	y= random.random()

	d = math.sqrt(x**2 + y**2)
	#print(x,y,d)
	total += 1
	if d < 1:
		inside += 1	
	pi_estimate = (inside / total) * 4
	print(pi_estimate)

	
	#variable that keeps track of points inside circle
	
	#these points/total  = pi/4
	#ratio of inside to total is pi/4

