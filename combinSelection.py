import math
def findCombination(n, r): #returns int value
	return (math.factorial(n)) / (math.factorial(r) * math.factorial(n-r))
def findValues(upper): #upper bound is 101
	count = 0
	for n in range(1, upper):
		for r in range(1, n):
			if(findCombination(n ,r) > 10**6): count += 1
	return count

print(findValues(101))