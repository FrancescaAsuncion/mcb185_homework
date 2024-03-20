"""
You may have heard of the 'birthday paradox' before. 
Write a program that simulates the problem by filling up classrooms of students with 
randomly chosen birthdays. Make the number of days in the calendar and the number of 
people in the classroom command line arguments. You will have to run this thousands of 
times to get an accurate estimate, so have a parameter for that too.

https://en.wikipedia.org/wiki/Birthday_problem

In this program, you must use a list for the birthdays. For example, 
if there are 23 people in the classroom, you will list.append() 23 times 
(unless you're extra-clever and figure out how to make a short-circuit).
"""

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


hits = 0

for x in range(trials): 
	bdays = [] #empty list of bdays for trials
	for j in range(people):
		bday = random.randint(0, days) #for each person, generate rand bday
		if bday in bdays: #if that bday is in list, +1
			hits += 1
			break
		else:
			bdays.append(bday) #adding bday to bdays list
		
print(hits/trials)
		
	
	
	
	

