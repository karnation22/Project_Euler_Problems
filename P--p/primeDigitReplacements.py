def isPrime(number):
	if(number < 2): return False
	for factor in range(2, int(number**0.5)+1):
		if(number%factor == 0): return False
	return True

def someCombination(prime, family): #work on ALL THE FUCKING REPLACEMENT COMBINATIONS! 
	
def primeDigitReplacements(prime, family): #arbitrarily start @ 10
	notFound = True
	while(notFound):
		prime += 1
		print(prime)
		if(isPrime(prime)): # check ALL combinations 
			if(someCombination(prime, family) != None): 
				notFound = False
	return prime



