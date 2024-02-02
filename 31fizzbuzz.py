# One of the classic interview questions is FizzBuzz. 
# Make a program that writes out the numbers from 1 to 100. 
# If the number is divisible by 3, write Fizz instead. 
# If the number is divisible by 5, write Buzz instead. 
#If the number is divisible by both 3 and 5, write FizzBuzz.

x = 0
for x in range(0,101):
	if x % 15 == 0:
		print("FizzBuzz")
	elif x % 5 == 0:
		print("Buzz")
	elif x % 3 == 0:
		print("Fizz")
	else:
		print(x)
	