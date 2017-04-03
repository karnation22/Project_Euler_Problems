def isPrime(number):
	if(number < 2): return False
	if(number == 2): return True
	for factor in range(2, int(number**0.5)+1):
		if(number%factor==0): return False
	return True

def isCircularPrime(number):
	strNum = str(number) #first convert number to string type
	numLen = len(strNum)
	for j in range(numLen):
		newStrNum = ""
		for i in range(numLen):
			if(i+j < numLen): newStrNum += strNum[i+j]
			else: newStrNum += strNum[(i+j)%numLen]
		if(not isPrime(int(newStrNum)) ): return False
	return True

def solvecircularPrime(limit):
	count = 0
	for number in range(limit):
		if(isCircularPrime(number)):
			print(number)
			count += 1
	return count

print(solvecircularPrime(10**6))