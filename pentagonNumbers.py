def isPentagonal(number): 
	#find the inverse function - determine if that is an int
	test = float((1 + (1 + 24*number)**0.5))
	test /= 6
	return test == int(test)

def createPentagonNumber(n): #takes int input
	return int(0.5*n*(3*n-1))

def findThePentagonal():
	answer = None
	first = 1
	notFound = True
	while(notFound):
		first += 1
		firstPent = createPentagonNumber(first)
		for second in range(first -1, 1, -1):
			secondPent = createPentagonNumber(second)
			if(isPentagonal(firstPent+secondPent) and isPentagonal(abs(firstPent - secondPent) ) ):
				answer = abs(firstPent - secondPent) #there is only one answer
				notFound = False
	return answer

print(findThePentagonal())
#5482660
