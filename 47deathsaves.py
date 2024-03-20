"""
Death saves are a little different than normal saving throws. 
If your health drops to 0 or below, you are unconscious and may die. 
Each time it is your turn, roll a d20 to determine if you get closer to life or fall deeper into death. 
If the number is less than 10, you record a "failure". 
If the number is 10 or greater, you record a "success". If you collect 3 failures, you "die". 
If you collect 3 successes, you are "stable" but unconscious. 
If you are unlucky and roll a 1, it counts as 2 failures. 
If you're lucky and roll a 20, you gain 1 health and have "revived". 
Write a program that simulates death saves. What is the probability one dies, stabilizes, or revives?
"""
import random
rolls = 10000

fail = 0
success = 0
die = 0
stabilize = 0 
revive = 0

for j in range(rolls):
	fail = 0
	success = 0
	while True:
		roll = random.randint(1, 20)
		if roll == 1: 
			fail += 2
		if roll == 20: 
			revive += 1
			break
		if roll >= 10: 
			success += 1
		else: 
			fail += 1
		
		if fail >= 3:
			die += 1
			break
		elif success >= 3: 
			stabilize += 1
			break
		
	


		
print(fail, success, revive)	
#print(die/rolls, stabilize/rolls)
			
	
print('Die:', die/rolls)
print('Stabilize:', stabilize/rolls)
print('Revive:', revive/rolls)
	