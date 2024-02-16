
import random
#random.random()
for i in range(5):
	print(random.random())

for i in range(50):
	print(random.choice('ACGT'), end='') #randomly chooses a letter from ACGT 50 times
print()

#sequences that are 70% AT on avg
for i in range(50):
	r = random.random()
	if r < 0.7: 
		print(random.choice('AT'), end='')
	else:
		print(random.choice('CG'), end='')
print()
	
#random number between two inclusive end points > ex: rolling 6 sided die 3 times
for i in range(3):
	print(random.randint(1,6))
	
#random.gauss()
for i in range(5):
	print(random.gauss(0.0,0.1))

"""	
#code review

# 42
import random

zerogames = 0
totalscore = 0
gamesplayed = 10000
for i in range(gamesplayed):
	score = 0
	for roundnum in range (2,13):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		if d1+d2 == roundnum:
			score += roundnum
			
	totalscore += score		
	if score == 0:
		zerogames += 1
		
print(zerogames/gamesplayed)
print(totalscore/gamesplayed)


nts = 'ACGT'
for nt in nts:
	print(nt, end=' ')
print()

import random
for i in range(3):
	print('>seq-', i, sep='')
	print(f '>seq-{i+1}')
	for i in range(random.randint(20,50)):
		print(random.choice(nts), end='')
	print()

nts = 'ACGT'
#print header	
for nt in nts:
	print(nt, end='')
print()

#print matrix
limit = len(nts)
for i in range(0, limit):
	for j in range(0, limit):
		if i == j: print('+', end='')
		else: print('-', end='')
		print()

total_4dr1 = 0 
for i in range(rolls):
	score = 0
	d1 = random.randint(1,6)
	# do d2-d4

print('this line\n has some\n line breaks')
print('a\tb\tcat\tdogma')
print(10, 20, 30, 40, sep='\t')
print(100, 2000, 30000, 40000, sep='\t')

i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi +pi}')

print(f'formatted string {i} {pi:.3f}')

"""
import sys
print('logging', file=sys.stderr)
		
	
	
	
	


