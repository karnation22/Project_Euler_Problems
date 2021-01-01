def isPrime(num):
	if(num < 2): return False
	if(num == 2): return True
	for factor in range(2,int(num**0.5)+1):
		if(num%factor == 0): return False
	return True

def FindSpiralPrimeCount(Thebreak): 
#HIGHLY INEFFICIENT ALGORITHM - WORK MORE ON IT
#NASTY AF CODE - WORK ON IT
	counter = 1 #after every four, we reset to zero
	primeCount = 0
	adder = 2 #after every four, we increment adder by two
	index = 3 #index initially starts @ 1 - increment by adder
	diagonal = 2; #increments by one every time
	length = 1
	while(True):
		if(isPrime(index)): primeCount += 1
		counter += 1
		diagonal += 1
		index += adder
		if(counter % 4 == 0): #after every four, we reset
			adder += 2
			length += 2
			counter = 0
		print(float(primeCount) / diagonal)
		if(counter == 0 and float(primeCount)/diagonal < 0.1): break
	return length

print(FindSpiralPrimeCount(48))