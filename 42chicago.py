import random
import sys

games = 1000000
log = games // 100 #report progress at 1% intervals
total = 0 
zeroes = 0
for i in range(games):
	if i % log == 0: print(f'{100 * i/games:.0f}', file=sys.stderr) #works with line 5 to display a status message each time 1% of the data has been processed.
	score = 0 # resets score every time a new game is played
	for target in range(2, 13): 
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	if score == 0: zeroes += 1 #intermediate calculations
	total += score
print(total / games)
print(zeroes / games)