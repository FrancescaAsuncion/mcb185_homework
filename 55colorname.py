"""
Write a program that provides the closest official color name given some red, green, and blue 
values. Each value must be in the range of 0-255. 
You will find color definitions in the colors_basic.tsv and colors_extended.tsv in MCB185/data.

Hint: this algorithm is not very different from minimum() except that the number you are 
trying to minimize is the difference between the input RGB values and those of a named color. 
You will have to keep track of both the minimum distance and the name of its corresponding color.

Hint: To calculate the distance between an input color and a named color, 
you can use taxi-cab distance. This is very similar to dkl() except that the loop sums up 
the absolute difference of each pair of values. It therefore doesn't assume probabilities 
or have problems with zero values.

"""

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])


def dtc(P, Q): #actual number and inputted
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d	

minimum = 1000
final_color = None

with open(colorfile, 'rt') as fp:
	for line in fp:
		words = line.split()
		color_name = words[0]
		for row in words:
			color_nums = words[2].split(',') #0 red; 1 green; 2 blue
			r = int(color_nums[0])
			g = int(color_nums[1])
			b = int(color_nums[2])
		d = dtc([R,G,B],[r,g,b]) 
		if d < minimum:
			minimum = d
			final_color = color_name
		#print(abs(R-r) + abs(G-g) + abs(B-b), color_name, dtc([R,G,B],[r,g,b]))
		
print(final_color)

