import math
from fractions import Fraction

# 1) write function to create continued fraction out of decimal number
# 2) create a set of valid D values as a function (just use filter and not isSquare)
# 3) for each number, find the continued fraction, chop the last element, and create decimal
# 4) if numerator of continued fraction is bigger than best, replace best

def foundRepeat(DecList, decD):
	return len(DecList) > 0 and abs(DecList[0] - decD) <= 1e-5

def buildNumList(D):
	(NumList, DecList) = ([math.floor(D**0.5)], [ ])
	decD = float(D**0.5) - math.floor(float(D**0.5)) 
	while(not(foundRepeat(DecList, decD))):
		NumList.append(math.floor(decD**-1)) 
		DecList.append(decD)
		decD = (decD**-1) - math.floor(decD**-1) 
	return NumList[:-1] #chop off that last number

print(buildNumList(661))

def validDvalues(lower, upper): #simply a list of valid D values
	return filter(lambda x: not (int(x**0.5)**2 == x))(num for num in range(lower,upper+1))


#now, find numerators and use simple current-best algorithm
