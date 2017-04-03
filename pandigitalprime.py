def sieve(limit):
	isPrime = [True]*(limit+1)
	isPrime[0] = isPrime[1] = False
	primes = [ ]
	for prime in range(2,limit+1):
		if(isPrime[prime]): primes.append(prime)
		for multiple in range(2*prime, limit+1, prime):
			isPrime[multiple] = False
	return primes #returns list value
def isPandigital(prime):
	digitCount = len(str(prime))
	listNum = [i for i in range(1, digitCount+1)] #gets all of the digits
	for digit in str(prime): #iterates through strings
		if(int(digit) not in listNum): return False
		listNum.remove(int(digit))
	return True


def findPandigital(limit):
	primes = sieve(limit) # get a list value
	maxPrime = None
	for prime in primes:
		if isPandigital(prime):
			if (maxPrime == None or prime > maxPrime): maxPrime = prime 
	return maxPrime

print(findPandigital(987654321))