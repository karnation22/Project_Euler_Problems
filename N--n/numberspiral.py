def getOnionCount(onion): #get contribution of each layer
	total = 0
	if(onion==0): return 1
	squareRoot = 2*onion+1
	square = int(squareRoot**2)
	subtractor = squareRoot - 1 
	for corner in range(4):
		total += square
		square -= subtractor
	return total


def findNumberSpiral(dimensions): #think bound divided by two plus one (3,2; 5,3; 7,4;)
	bound = dimensions//2 +1
	print(bound)
	total = 0
	for onion in range(bound): #we want 0, 1, 2 for the first case
		total += getOnionCount(onion)
	return total

print(findNumberSpiral(1001))
