"""
This is the same problem as above, but instead of making a list of birthdays (e.g. 23) 
make a list from the calendar (e.g. 365). In the previous program, you appended 
birthdays to a list. In this one, all possible days are already in a list, so assigning a 
birthday is: calendar[birthday] += 1.
"""

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def bcal(trials, days, people):
	same_trials = 0
	for i in range(trials):
		calendar = []
		for x in range(days): 
			calendar.append(0)
	
		for j in range(people):
			calendar[random.randint(0, days - 1)] += 1
		
		same_bday = False
		for c in calendar:
			if c > 1: 
				same_bday = True
				break
				
		if same_bday: same_trials += 1
				
	prob = (same_trials / trials)
	return prob

p = bcal(trials, days, people)
print(p)
		
