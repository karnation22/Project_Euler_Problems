def factorial(digit):
	if(digit==0): return 1
	else: return digit*factorial(digit-1)

def isDigitFactorial(number):
	facSum = 0
	strNum = str(number)
	for digit in strNum: #goes through number as a string
		facSum += factorial(int(digit)) #takes in integer type
	return (facSum==number)
def determineSum(lower, upper):
	sum = 0
	for number in range(lower, upper):
		if(isDigitFactorial(number)): 
			print(number)
			sum += number
	return sum

print(determineSum(10, 5*10**4))
