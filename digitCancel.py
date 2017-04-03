def isCurious(numerator, denominator): #returns true for trivial examples as well
	floatFraction = float(numerator) / denominator #stores float value
	(strNum, strDen) = (str(numerator) , str(denominator) )
	(charNum, charNum2, charDem, charDem2) = (strNum[0], strNum[1], strDen[1], strDen[0])
	if(int(charDem) != 0): newFloat = float(int(charNum)) / float(int(charDem))
	else: newFloat = None
	return(newFloat != None and floatFraction == newFloat and charNum2==charDem2) #can compare string types

def isRepeat(numerator, denominator):
	(strNum, strDen) = (str(numerator), str(denominator))
	return(strNum[0] == strNum[1] and strDen[0] == strDen[1])

def makeFactorSet(number):
	factorSet = set()
	for factor in range(1, number+1): #includes the number itself
		if(number%factor==0): factorSet.add(factor)
	return factorSet #returns set of all factors
	

def findFourFractions(lower, upper): #returns a list of four numerator/denominator tuples
	fractionList = [ ]
	for numerator in range(lower, upper + 1):
		for denominator in range(numerator+1, upper+1): #denominator > numerator
			if(isCurious(numerator, denominator) and not isRepeat(numerator, denominator)): 
				fractionList.append((numerator, denominator))
	return fractionList

def determineType(lower, upper):
	fractionList = findFourFractions(lower, upper)
	numerator = 1
	denominator = 1
	for (num, den) in fractionList:
		numerator *= num
		denominator *= den
	floatFraction = float(numerator) / denominator
	(maxFactor, bestFraction) = (None, None) #will convert to tuple type
	numFact = makeFactorSet(numerator)
	denFact = makeFactorSet(denominator)
	intSet = numFact.intersection(denFact)
	for factor in intSet:
		newFloat = float(int(numerator/factor)) / int(denominator/factor)
		if( (maxFactor == None or factor > maxFactor) and (newFloat==floatFraction) ):
			maxFactor = factor
			bestFraction = (numerator/factor, denominator/factor)

	return bestFraction

print(determineType(10, 100))
