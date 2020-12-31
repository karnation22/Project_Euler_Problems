def findAllTruncatables(lower, upper):
	maxSolutions = None
	maxResult = None
	for p in range(lower, upper):
		for a in range(2, int(p/3)):
			currentSolutions = 0
			if(p*(p-(2*a)) % (2*(p-a)) == 0): currentSolutions += 1
		if(maxSolutions == None or currentSolutions > maxSolutions):
			print(p) 
			maxSolutions = currentSolutions
			maxResult = p
	return maxResult

print(findAllTruncatables(10, 10**3))


