import itertools
#determine the extreme brute force way of doing this
def sieve(n):
    isPrime = [ True ] * (n+1) # assume all are prime to start
    isPrime[0] = isPrime[1] = False # except 0 and 1, of course
    primes = [ ]
    for prime in range(n+1):
        if (isPrime[prime] == True):
            # we found a prime, so add it to our result
            primes.append(prime)
            # and mark all its multiples as not prime
            for multiple in range(2*prime, n+1, prime):
                isPrime[multiple] = False
    return primes

def isPrime(num):
	if(num < 2): return False
	if(num == 2): return True
	for factor in range(2, int(num**0.5) + 1):
		if(num%factor == 0): return False
	return True

def determineLargestPrime(primeList, start):
	total = 0
	sublist = list()
	index = start
	while (total < 10**6): #if we start from 2, we HAVE to go to the largest prime
		total += primeList[index] 
		if(isPrime(total)): sublist.append(total)
		index += 1
	return sublist[-1] #return largest prime in that sublist

#1) determine sublist that is less than one million
#2) determine length of sublist
#3) keep shifting index until it breaks
def consecPrimeSolver(upper): ##KEY WORD IS CONSECUTIVE!!!!!
	#Main Program
	primeList = sieve(upper) #get list of primes from 1-->10**6
	(maxPrime, largestPrime, start) = (0, 0, 0)
	while(largestPrime < 10**6): #stops the process from running indefinately
		largestPrime = determineLargestPrime(primeList, start)
		if(largestPrime < 10**6 and largestPrime > maxPrime): maxPrime = largestPrime
		#^ stops from actually allowing maxPrime to exceed 10**6
		start += 1
	return maxPrime
print(consecPrimeSolver(10**6))


