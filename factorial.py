def factorial(n):
	fact = 1
	for num in range(1, n+1):
		fact *= num
		print("at " + str(num) + " we have " + str(fact))
	return fact

def 