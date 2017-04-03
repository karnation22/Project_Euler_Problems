#method that determines if a number is lychel
#isLychrel works through 50 iterations 

def isLychrel(number): #returns True if there is a palindrome, false otherwise
	iterCount = 50
	while(iterCount > 0): #assume false if not reached in 50 iterations
		revNumber = str(number)[::-1] #essentially reverses the string
		number = int(revNumber) + number #modify old number
		if(str(number) == str(number)[::-1]): return False
		iterCount -=1
	return True #is lychrel if makes it out of while loop

def findLychrelCount(upper): #inputs 10**4 upper limit
	lychrelCount = 0
	for number in range(1, upper):
		if(isLychrel(number)): lychrelCount += 1
	return lychrelCount

print(findLychrelCount(10**4))