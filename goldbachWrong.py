def isPrime(number):
	if(number < 2): return False
	if(number == 2): return True
	for factor in range(2, int(number**0.5) + 1):
		if(number%factor == 0): return False
	return True

def isSquare(number):
	return (number == int(number**0.5)**2)

def sieve(n):
    isPrime = [ True ] * (n+1) # assume all are prime to start
    isPrime[0] = isPrime[1] = False # except 0 and 1, of course
    primes = [ ]
    for prime in range(n+1):
        if (isPrime[prime] == True): # we found a prime, so add it to our result
            primes.append(prime) # and mark all its multiples as not prime
            for multiple in range(2*prime, n+1, prime):
                isPrime[multiple] = False
    return primes

def isGoldbach(smallest, listPrimes): #smallest int, and iterate through
	for prime in listPrimes: #iterate through list
		if(isSquare(0.5*(smallest-prime))): return True
	return False 

def findSmallestWrong():
	notFound = True
	smallest = 1 #start with the smallest
	while(notFound):
		print(smallest)
		smallest += 2 #only working w/ odd numbers
		if(not isPrime(smallest)): #only work with non primes
			listPrimes = sieve(smallest) #returns list of all primes smaller 
			if(not isGoldbach(smallest, listPrimes)): notFound = False
	return ("the smallest is " + str(smallest))

print(findSmallestWrong()) #5777