def createPanDigital(number):
	strNum = ""
	counter = 1
	while(len(strNum) < 9):
		strNum += str(number*counter)
		counter += 1
	return int(strNum)
print(createPanDigital(92))

def isPanDigital(panDigitalNumber):
	listNum = [1,2,3,4,5,6,7,8,9]
	if(len(str(panDigitalNumber)) != 9): return False
	for strDig in str(panDigitalNumber):
		if(int(strDig) not in listNum): return False
		listNum.remove(int(strDig))
	return True

def findLargestPandigital(lower, upper): #start at 9  and go until  100,000
	maxPan = None
	for number in range(lower, upper): #we go by number, NOT pandigital
		panDigitalNumber = createPanDigital(number) #return a number w/ at least nine digits
		if(isPanDigital(panDigitalNumber)):
			if(maxPan==None or panDigitalNumber > maxPan): maxPan = panDigitalNumber
	return maxPan
print(findLargestPandigital(9, 100000))



