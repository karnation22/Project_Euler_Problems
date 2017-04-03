def isPrime(number):
	if(number < 2): return False
	elif(number==2): return True
	for factor in range(2, int(number**0.5)+1):
		if(number%factor==0): return False
	return True

def isLeftTruncatable(trunc):
	strtrun = str(trunc)
	while(len(strtrun) > 0): 
		if(not isPrime(int(strtrun) ) ): return False
		strtrun = strtrun[1:]
	return True

def isRightTruncatable(trunc):
	strtrun = str(trunc)
	while(len(strtrun) > 0):
		if(not isPrime(int(strtrun))): return False
		strtrun = strtrun[:-1]
	return True

def findSum(lower, upper): #give two ints of lower and upper limits
	setSum = set()
	for trunc in range(lower, upper):
		if(isLeftTruncatable(trunc) and isRightTruncatable(trunc)):
			setSum.add(trunc)
	return (setSum, sum(setSum))

print(findSum(10, 10**6))