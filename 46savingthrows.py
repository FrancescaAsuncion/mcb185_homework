"""
One of the core mechanics of D&D is the "saving throw". 
When certain events happen, you need to roll a d20 to figure out if you succeed or not. 
For example, you are walking across a frozen lake and it begins to crack underfoot. 
If you make a saving throw, you step aside. 
If you fail, you fall in. Some saving throws are more difficult than others. 
If the ice is very thick, the "difficulty class" (DC) may be only 5. 
This means you only need to roll a 5 or higher to succeed. 
However, if the ice is thin and has a DC of 15, you will need a roll of 15 or higher to succeed. 
Certain events may give you "advantage" or "disadvantage". 
For example, if you have a rope tied around your waist and a friend is instructed 
to pull you aside if anything bad happens, you could have "advantage". 
This allows you to roll two d20s and take the larger value. 
You may also have disadvantage, for example another "friend" pushes you from behind, 
causing you to stumble forward. In this case, you have "disadvantage" and 
must take the lower of two d20 rolls.

Write a program that simulates saving throws against DCs of 5, 10, and 15. 
What is the probability of success normally or with advantage/disadvantage? 
Make a table showing the results.

#roll a die and compare to DC, lower is a failure


5 is 20% chance you fail 
10 is 45% chance you fail 55% success
15 is 70% chance you fail 30% success

find averages
roll one of each kind, normal, advantage, disadvantage > functions

"""

import random

rolls = 10000

def normal(x):
	fail = 0
	success = 0
	for i in range(rolls):
		roll = random.randint(1, 20)
		if roll >= x: 
			success += 1
		else:
			fail += 1		
	return success / rolls
	
#print(normal(5))
#print(normal(10))
#print(normal(15))

def advantage(x):
	fail = 0
	success = 0
	for i in range(rolls):
		roll_1 = random.randint(1, 20)
		roll_2 = random.randint(1, 20)
		if roll_1 <= x:
			success += 1
		elif roll_2 >= x:
			success += 1
		else:
			fail += 1
	return success / rolls

#print(advantage(5))
#print(advantage(10))
#print(advantage(15))



def disadvantage(x):
	fail = 0
	success = 0
	for i in range(rolls):
		roll_1 = random.randint(1, 20)
		roll_2 = random.randint(1, 20)
		if roll_1 <= roll_2 and roll_1 >= x:
			success += 1
		elif roll_2 <= roll_1 and roll_2 >= x:
			success += 1
		else:
			fail += 1
	return success / rolls


#print(disadvantage(5))
#print(disadvantage(10))
#print(disadvantage(15))


print('DC\tnorm\tadv\tdis')
print('5', normal(5), advantage(5), disadvantage(5), sep='\t' )
print('10', normal(10), advantage(10), disadvantage(10), sep='\t' )
print('15', normal(15), advantage(15), disadvantage(15), sep='\t')
