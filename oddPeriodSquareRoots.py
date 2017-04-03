import math

#find period function returns an int of the period 
## 1) first it cleaves off the initial int portion of the number
## 2) then it chuck the number into the helper findSequence
## 3) after findPeriod gets that int list, we simply return the int list's period

def isEpsiEqual(flo1, flo2):
	return abs(flo1 - flo2) <= 1e-5

def foundRepeat(numflo, numfloList):
	return len(numfloList) > 0 and isEpsiEqual(numflo, numfloList[0])

def findSequence(numflo): 
	#takes a float 0 < numflo < 1, and generates sequence
	numfloList = [ ]
	while(not(foundRepeat(numflo,numfloList))):
		numfloList.append(numflo)
		numflo = (numflo**-1) - math.floor(numflo**-1)
	return numfloList

def findPeriod(num):
	numflo = (float(num)**0.5) - math.floor(float(num)**0.5)
	return len(findSequence(numflo))
	#numflo is now a float with just a positive decimal portion

def isSquare(num): #takes int, outputs a boolean
	return (num**0.5)**2 == num

def totalCountMain(start, end):
	return len(filter((lambda number : not(isSquare(number)) and findPeriod(number)%2==1), 
			[num for num in range(start, end+1)]))

##too long of an algorithm - implement the other one if you want