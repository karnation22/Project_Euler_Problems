def isPrime(num):
	if(num < 2): return False
	for factor in range(2, int(num**0.5)+1):
		if(num%factor==0): return False
	return True

def only2And5(num): #determine all of the prime factors of int greater than 1
	pSet = set()

	if(num == 2 or num==5 or num==1): return True
	for sub in range(2, num//2+1):
		if(isPrime(sub) and num%sub==0): pSet.add(sub)
	return pSet == set([2]) or pSet == set([5]) or pSet == set([2,5])

def digitCount(number):
	count=0
	while(number > 0):
		count += 1
		number//=10
	return count
def determineRepeat(reciprocal, number): #reciprocal is a float value
	index = 0
	reciprocal *= 10**(digitCount(number)-1)
	while(True):
		reciprocal *= 10
		print(int(reciprocal), int((reciprocal%1)*(10**(index+1))) )
		if(int(reciprocal) == int((reciprocal%1)*(10**(index+1))) and int(reciprocal)!=0): 
			return index+1
		index += 1
def maxReciprocal(limit):
	MaxRep = 0
	for num in range(limit):
		num = num+1
		if(not only2And5(num) and num!= 1): #it is prime or includes more than two and five
			reciprocal = 1/float(num)
			MaxRep = determineRepeat(reciprocal)
	return MaxRep

print(determineRepeat(1/float(51), 13))

	



