def isPrime(number):
	if(number < 2): return False
	if(number == 2): return True
	for factor in range(2, int(number**0.5) + 1):
		if(number%factor == 0): return False
	return True

def numberOfPrimes(number):
	primeSet = set()
	while(not isPrime(number)):
		for prime in range(2, int(number**0.5)+1):
			if(isPrime(prime) and number%prime==0): 
				primeSet.add(prime)
				number /= prime
				break
	primeSet.add(number) #add the final prime number	
	return len(primeSet) #returns number of primes 

def findFourDistinctPrimes():
	fourConsec = [ ] #list of numbers (we need four in a row w/ four distinct primes)
	index = 1000
	while(len(fourConsec) < 4): #keep going
		index += 1
		print(index)
		if(numberOfPrimes(index) == 4): 
			print("I entered here")
			fourConsec.append(index)
		else: fourConsec = [ ] #make it an empty list again
	return fourConsec #returns list w/ four numbers

print(findFourDistinctPrimes())