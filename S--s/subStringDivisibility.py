from itertools import permutations


def hasProperty(number, listNum): #string and list
	for i in range(7):#don't we love magic numbers?
		substrNum = number[1+i:4+i]
		if(int(substrNum) % listNum[i] != 0): return False
	return True
		
def subStringDivisibility():
	sum = 0
	primes = [2,3,5,7,11,13,17]
	for number in permutations([str(x) for x in range(10)]):
		number = ''.join(number)
		if(hasProperty(number, primes)): sum += int(number)
		
	return sum

print(subStringDivisibility())
