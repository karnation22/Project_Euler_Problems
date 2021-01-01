def getPrimes(limit):
	lPrime = [True]*(limit+1)
	lPrime[0]=lPrime[1] = False
	primes = [ ]
	for prime in range(limit+1):
		if(lPrime[prime] == True): #found a prime
			primes.append(prime)
			for multiple in range(2*prime, limit+1, prime):
				lPrime[multiple] = False
	return primes #returns a list of primes


def isPrime(num):
	if(num < 2): return False
	if(num == 2): return True
	for factor in range(2, num):
		if(num%factor==0): return False
	return True

def getPrimeCount(indexA, indexB):
	count = 1
	while(True):
		quadratic = count**2 + indexA*count + indexB
		if(isPrime(quadratic)): count+=1
		else: break
	return count
def prod(tuple):
    final = 1
    for num in tuple:
        final *= num
    return final

def solveQuadratic(bounds): #1000 is the bounds value
	maxScore = 0
	maxNumbers = None
	primes = getPrimes(bounds)
	for indexA in range(-bounds,bounds+1): #-1000 --> 1000 inclusive
		for indexB in primes: #we know indexB is prime b/c n=0
			if(isPrime(indexA + indexB + 1)):  # n=1 they have to be prime to begin
				currentScore = getPrimeCount(indexA, indexB)
				print(indexA, indexB)
				if(currentScore > maxScore): 
					maxScore = currentScore
					maxNumbers = (indexA, indexB)
	return prod(maxNumbers)
print(solveQuadratic(1000))



