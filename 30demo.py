"""
n = 0 #initialization condition
def chksum(s):
	n = 0
	for c in s:
		n = n + ord(c)
	return n % 256
print(chksum('Francesca'))



#get maximum value between the letters
def maxchar(s):
	mx = 0 # set to the lowest 
	for c in s:
		if ord(c) > mx:
			mx = ord(c)
	return mx

def minchar(s):
	minx = 255 # set it to the highest 
	for c in s:
		if ord(c) < minx:
			minx = ord(c)
	return minx	
	
name = 'natalia'
print(chksum(name))
print(maxchar(name))
print(minchar(name))

import math
def euler(limit):
	e = 0
	for n in range (limit):
		e = e + 1 / math.factorial(n)
		print (e)
	return e
print(euler(10))


for char in 'hello':
	print(char)
	

seq = 'GAATTC'
for a in seq:
	print(a)
	
#use math factorial for n choose k

"""
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)