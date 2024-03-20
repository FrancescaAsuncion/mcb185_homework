"""
In Dungeons and Dragons, each character is described by 6 statistics 
(strength, intelligence, wisdom, dexterity, constitution, charisma). 
In the old days, each stat was decided by summing up the values on 3 six-sided dice (3D6). 
Each stat therefore has a range of 3-18 and an average of 10.5. 
Over the years, the official rules have changed and many players have added their own house rules. 
Write a program that determines the average stat value using the various rules below.

3D6: roll 3 six-sided dice
3D6r1: roll 3 six-sided dice, but re-roll any 1s
3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
4D6d1: roll 4 six-sided dice, dropping the lowest die roll
"""
#done

import random

#3D6: roll 3 six-sided dice
rolls = 100000
score = 0

for i in range(rolls):
	for x in range(3):
		r = random.randint(1, 6)
		score += r
print(score / rolls)

#3D6r1: roll 3 six-sided dice, but re-roll any 1s
rolls = 100000
totals = 0

for i in range(rolls):
	for x in range(3):
		r = random.randint(1, 6)
		if r == 1:
			r = random.randint(1, 6)
		totals += r
print(totals / rolls)

#3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
rolls = 100000
totals = 0

for i in range(rolls):
	score = 0
	for x in range(3):
		roll_1 = random.randint(1, 6)
		roll_2 = random.randint(1, 6)
		if roll_1 > roll_2:
			score += roll_1
		else:
			score += roll_2
	totals += score
print(totals / rolls)

#4D6d1: roll 4 six-sided dice, dropping the lowest die roll
rolls = 100000
score = 0
mini_die = 7
totals = 0

for i in range(rolls):
	for i in range(4):
		r = random.randint(1,6)
		totals += r
		if r < mini_die:
			mini_die = r
	score = totals - mini_die
print(score / rolls)


"""
	score = 0 
	r = 1
	for d in range(3):
		roll = random.randint(1, 6)
		if roll > r:
			score += roll
	totals += score
print(totals / rolls)
"""	
		

